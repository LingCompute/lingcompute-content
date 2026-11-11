import io
import json
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

from tools import review_gate


def review(login="expert", state="APPROVED", commit="current", identifier=1, kind="User"):
    return {
        "id": identifier, "user": {"login": login, "type": kind},
        "state": state, "commit_id": commit,
    }


def response(data):
    return io.BytesIO(json.dumps(data).encode())


class ReviewTests(unittest.TestCase):
    def test_only_non_author_human_current_approval_counts(self):
        reviews = [
            review(), review("author"), review("robot", kind="Bot"),
            review("stale", commit="previous"),
        ]
        self.assertEqual(review_gate.approvals(reviews, "Author", "current"), {"expert"})

    def test_dismissal_or_changes_requested_revokes_approval(self):
        for state in ("DISMISSED", "CHANGES_REQUESTED"):
            with self.subTest(state=state):
                self.assertEqual(review_gate.approvals(
                    [review(), review(state=state, identifier=2)], "author", "current",
                ), set())

    def test_comment_preserves_prior_substantive_review(self):
        self.assertEqual(review_gate.approvals(
            [review(), review(state="COMMENTED", identifier=2)], "author", "current",
        ), {"expert"})

    def test_roster_is_product_specific_and_fails_closed(self):
        files = ["content/photon/one/article.md", "content/fluid/one/figure.png"]
        self.assertEqual(review_gate.missing_reviews(
            files, [review()], {"photon": ["Expert"], "fluid": []}, "author", "current",
        ), ["fluid"])
        self.assertEqual(review_gate.missing_reviews(
            ["content/new/one/article.md"], [review()], {}, "author", "current",
        ), ["new"])
        self.assertEqual(review_gate.missing_reviews(
            ["tools/style.css"], [], {}, "author", "current",
        ), [])

    @patch.object(review_gate, "github_pages")
    @patch.object(review_gate, "urlopen")
    def test_rename_checks_both_old_and_new_product(self, api, pages):
        pull = {
            "state": "open", "head": {"sha": "current"}, "base": {"sha": "base"}, "changed_files": 1,
            "user": {"login": "author"},
        }
        manifest = {"articles": [{"slug": "article", "authors": ["writer"]}]}
        api.side_effect = [
            response(pull), response({}), response(manifest),
            HTTPError("url", 404, "missing", None, None), response(manifest),
            response(pull), response({}),
        ]
        pages.side_effect = [[{
            "filename": "content/fluid/new/article.md",
            "previous_filename": "content/photon/old/article.md",
            "status": "renamed",
        }], [review()]]
        review_gate.check_pull(1, "owner/repo", "token", {"fluid": ["expert"]})
        status = json.loads(api.call_args.args[0].data)
        self.assertEqual(status["state"], "failure")
        self.assertIn("photon", status["description"])

    @patch.object(review_gate, "urlopen")
    def test_shared_asset_excludes_every_declared_series_author(self, api):
        api.return_value = response({"articles": [
            {"slug": "first", "authors": ["Expert"]},
            {"slug": "second", "authors": ["Other"]},
            {"slug": "historical", "authors": []},
        ]})
        files = ["content/photon/one/figures/shared.png"]
        authors = review_gate.series_authors(
            [{"filename": files[0], "status": "modified"}],
            {"head": {"sha": "current"}}, "owner/repo", "token",
        )
        self.assertEqual(authors, {"photon": {"expert", "other"}})
        self.assertEqual(review_gate.missing_reviews(
            files, [review(), review("other", identifier=2)],
            {"photon": ["expert", "other"]}, "editor", "current", authors,
        ), ["photon"])
        self.assertEqual(review_gate.missing_reviews(
            files, [review("independent")], {"photon": ["independent"]},
            "editor", "current", authors,
        ), [])
        request = api.call_args.args[0]
        self.assertEqual(request.full_url,
                         "https://api.github.com/repos/owner/repo/contents/content/photon/one/series.json?ref=current")
        self.assertEqual(request.get_header("Accept"), "application/vnd.github.raw+json")

    @patch.object(review_gate, "urlopen")
    def test_direct_article_edits_require_nonempty_authors(self, api):
        for status in ("added", "modified", "renamed"):
            for entry in ({}, {"slug": "article"}, {"slug": "article", "authors": []}):
                with self.subTest(status=status, entry=entry):
                    api.return_value = response({"articles": [entry] if entry else []})
                    with self.assertRaises(ValueError):
                        review_gate.series_authors(
                            [{"filename": "content/photon/one/article.md", "status": status, "changes": 1}],
                            {"head": {"sha": "current"}}, "owner/repo", "token",
                        )

    @patch.object(review_gate, "urlopen")
    def test_direct_article_authors_excluded_even_when_editor_opens_pr(self, api):
        api.return_value = response({"articles": [{"slug": "article", "authors": ["Expert"]}]})
        files = ["content/photon/one/article.md"]
        authors = review_gate.series_authors(
            [{"filename": files[0], "status": "modified"}],
            {"head": {"sha": "current"}}, "owner/repo", "token",
        )
        self.assertEqual(review_gate.missing_reviews(
            files, [review()], {"photon": ["expert"]}, "editor", "current", authors,
        ), ["photon"])

    @patch.object(review_gate, "urlopen")
    def test_pure_rename_allows_unknown_historical_authors(self, api):
        api.return_value = response({"articles": [{"slug": "article", "authors": []}]})
        self.assertEqual(review_gate.series_authors(
            [{"filename": "content/photon/one/article.md",
              "previous_filename": "content/photon/one/old.md", "status": "renamed", "changes": 0}],
            {"head": {"sha": "current"}}, "owner/repo", "token",
        ), {"photon": set()})

    @patch.object(review_gate, "urlopen")
    def test_metadata_and_sources_allow_unknown_historical_authors_but_need_roster(self, api):
        for filename in ("series.json", "SOURCES.md", "README.md", "figures/plot.png"):
            with self.subTest(filename=filename):
                api.return_value = response({"articles": [{"slug": "historical", "authors": []}]})
                files = [f"content/photon/one/{filename}"]
                authors = review_gate.series_authors(
                    [{"filename": files[0], "status": "modified"}],
                    {"head": {"sha": "current"}}, "owner/repo", "token",
                )
                self.assertEqual(review_gate.missing_reviews(
                    files, [], {"photon": ["expert"]}, "editor", "current", authors,
                ), ["photon"])
                self.assertEqual(review_gate.missing_reviews(
                    files, [review()], {"photon": ["expert"]}, "editor", "current", authors,
                ), [])

    @patch.object(review_gate, "urlopen")
    def test_deleted_series_uses_base_authors_or_pr_author_only_when_absent(self, api):
        for base in ({"articles": [{"slug": "article", "authors": ["Expert"]}]}, None):
            with self.subTest(base=base):
                api.side_effect = [
                    HTTPError("url", 404, "missing", None, None),
                    response(base) if base else HTTPError("url", 404, "missing", None, None),
                ]
                authors = review_gate.series_authors(
                    [{"filename": "content/photon/one/article.md", "status": "removed"}],
                    {"head": {"sha": "current"}, "base": {"sha": "base"}},
                    "owner/repo", "token",
                )
                self.assertEqual(authors, {"photon": {"expert"}} if base else {})
                self.assertTrue(api.call_args.args[0].full_url.endswith("?ref=base"))

    @patch.object(review_gate, "urlopen")
    def test_missing_head_manifest_for_article_and_other_api_errors_fail_closed(self, api):
        for status, code in (("modified", 404), ("removed", 403), ("modified", 500)):
            with self.subTest(status=status, code=code):
                api.side_effect = HTTPError("url", code, "error", None, None)
                api.reset_mock()
                with self.assertRaises(HTTPError):
                    review_gate.series_authors(
                        [{"filename": "content/photon/one/article.md", "status": status}],
                        {"head": {"sha": "current"}, "base": {"sha": "base"}},
                        "owner/repo", "token",
                    )
                self.assertEqual(api.call_count, 1)

    @patch.object(review_gate, "urlopen")
    def test_invalid_author_declarations_fail_closed(self, api):
        for authors in ("expert", None, [""], [" expert"], [17]):
            with self.subTest(authors=authors):
                api.return_value = response({"articles": [{"slug": "article", "authors": authors}]})
                with self.assertRaises(ValueError):
                    review_gate.series_authors(
                        [{"filename": "content/photon/one/series.json", "status": "modified"}],
                        {"head": {"sha": "current"}}, "owner/repo", "token",
                    )

    @patch.object(review_gate, "urlopen")
    def test_invalid_manifest_structure_fails_closed(self, api):
        for manifest in (None, [], "manifest", {}, {"articles": None}, {"articles": {}},
                         {"articles": "article"}, {"articles": [None]}, {"articles": [[]]},
                         {"articles": ["article"]}, {"articles": [{}]}):
            with self.subTest(manifest=manifest):
                api.return_value = response(manifest)
                with self.assertRaises(ValueError):
                    review_gate.series_authors(
                        [{"filename": "content/photon/one/series.json", "status": "modified"}],
                        {"head": {"sha": "current"}}, "owner/repo", "token",
                    )

    @patch.object(review_gate, "urlopen")
    def test_invalid_article_slugs_fail_closed_even_without_authors(self, api):
        for slug in (None, 17, [], {}, "", " article", "../article", "Article", "one--two", "article\n"):
            with self.subTest(slug=slug):
                api.return_value = response({"articles": [{"slug": slug, "authors": []}]})
                with self.assertRaises(ValueError):
                    review_gate.series_authors(
                        [{"filename": "content/photon/one/series.json", "status": "modified"}],
                        {"head": {"sha": "current"}}, "owner/repo", "token",
                    )

    @patch.object(review_gate, "urlopen")
    def test_refresh_rejects_malformed_first_pr_and_continues_to_next(self, api):
        first = {"state": "open", "head": {"sha": "malformed"}, "changed_files": 1,
                 "user": {"login": "editor"}}
        second = dict(first, head={"sha": "valid"})
        changed = [{"filename": "content/photon/one/article.md", "status": "modified"}]
        manifests = [
            {"articles": [None]},
            {"articles": [{"slug": "article", "authors": ["writer"]}]},
        ]
        responses = [response([{"number": 1}, {"number": 2}])]
        for pull, manifest in zip((first, second), manifests):
            responses.extend(response(data) for data in (
                pull, {}, changed, [review(commit=pull["head"]["sha"])], manifest, pull, {},
            ))
        api.side_effect = responses
        with patch.dict(review_gate.os.environ, {
            "GITHUB_EVENT_PATH": "event.json", "GITHUB_REPOSITORY": "owner/repo", "GH_TOKEN": "token",
        }), patch.object(review_gate.Path, "read_text", side_effect=[
            json.dumps({"workflow_run": {"pull_requests": []}}),
            json.dumps({"photon": ["expert"]}),
        ]):
            self.assertEqual(review_gate.main(), 0)
        statuses = [
            (request.full_url.rsplit("/", 1)[-1], json.loads(request.data))
            for call in api.call_args_list
            if (request := call.args[0]).data is not None
        ]
        self.assertEqual([(commit, status["state"]) for commit, status in statuses], [
            ("malformed", "pending"), ("malformed", "failure"),
            ("valid", "pending"), ("valid", "success"),
        ])
        self.assertIn("Invalid article", statuses[1][1]["description"])

    @patch.object(review_gate, "urlopen")
    def test_contents_path_is_encoded_and_series_fetched_once(self, api):
        api.return_value = response({"articles": []})
        review_gate.series_authors(
            [{"filename": f"content/photon/one?#/{filename}", "status": "modified"}
             for filename in ("SOURCES.md", "README.md")],
            {"head": {"sha": "current"}}, "owner/repo", "token",
        )
        self.assertEqual(api.call_count, 1)
        self.assertIn("/one%3F%23/series.json?ref=current", api.call_args.args[0].full_url)

    @patch.object(review_gate, "github_pages", return_value=[])
    @patch.object(review_gate, "urlopen")
    def test_recheck_skips_final_status_when_head_changes_or_pr_closes(self, api, pages):
        pull = {"state": "open", "head": {"sha": "current"}, "changed_files": 0,
                "user": {"login": "author"}}
        for current in (dict(pull, head={"sha": "new"}), dict(pull, state="closed")):
            with self.subTest(current=current):
                api.reset_mock()
                api.side_effect = [response(pull), response({}), response(current)]
                review_gate.check_pull(1, "owner/repo", "token", {})
                requests = [call.args[0] for call in api.call_args_list]
                statuses = [request for request in requests if request.data is not None]
                self.assertEqual(len(statuses), 1)
                self.assertEqual(json.loads(statuses[0].data)["state"], "pending")
                self.assertTrue(statuses[0].full_url.endswith("/statuses/current"))

    @patch.object(review_gate, "github_pages", return_value=[])
    @patch.object(review_gate, "urlopen")
    def test_recheck_publishes_only_at_the_unchanged_captured_head(self, api, pages):
        pull = {"state": "open", "head": {"sha": "current"}, "changed_files": 0,
                "user": {"login": "author"}}
        api.side_effect = [response(pull), response({}), response(pull), response({})]
        review_gate.check_pull(1, "owner/repo", "token", {})
        self.assertTrue(api.call_args.args[0].full_url.endswith("/statuses/current"))
        self.assertEqual(json.loads(api.call_args.args[0].data)["state"], "success")

    @patch.object(review_gate, "series_authors", side_effect=ValueError("Missing authors"))
    @patch.object(review_gate, "github_pages")
    @patch.object(review_gate, "github")
    def test_missing_authors_produces_explicit_failure_status(self, api, pages, authors):
        api.return_value = {
            "state": "open", "head": {"sha": "current"}, "changed_files": 1,
            "user": {"login": "editor"},
        }
        pages.side_effect = [[{"filename": "content/photon/one/article.md", "status": "added"}], []]
        review_gate.check_pull(1, "owner/repo", "token", {})
        self.assertEqual(api.call_args.args[3]["state"], "failure")
        self.assertIn("Missing authors", api.call_args.args[3]["description"])

    @patch.object(review_gate, "github_pages", return_value=[])
    @patch.object(review_gate, "github")
    def test_incomplete_changed_files_cannot_approve(self, api, pages):
        api.return_value = {
            "state": "open", "head": {"sha": "current"}, "changed_files": 3001,
            "user": {"login": "author"},
        }
        with self.assertRaises(ValueError):
            review_gate.check_pull(1, "owner/repo", "token", {})
        self.assertEqual(api.call_args.args[3]["state"], "pending")

    @patch.object(review_gate, "github")
    def test_pagination_preserves_existing_query(self, api):
        api.side_effect = [[{"number": number} for number in range(100)], []]
        self.assertEqual(len(review_gate.github_pages("pulls?state=open", "owner/repo", "token")), 100)
        self.assertEqual(api.call_args_list[1].args[0], "pulls?state=open&per_page=100&page=2")


if __name__ == "__main__":
    unittest.main()
