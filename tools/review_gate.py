import json
import os
import re
import sys
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


def products_changed(files):
    return {
        parts[1]
        for filename in files
        if len(parts := filename.split("/")) >= 3 and parts[0] == "content"
    }


def approvals(reviews, author, commit):
    latest = {}
    for review in sorted(reviews, key=lambda item: item["id"]):
        user = review["user"]
        if review["state"] == "COMMENTED":
            continue
        latest[user["login"].lower()] = review
    return {
        login
        for login, review in latest.items()
        if review["state"] == "APPROVED"
        and review["commit_id"] == commit
        and review["user"]["type"] == "User"
        and login != author.lower()
    }


def missing_reviews(files, reviews, roster, author, commit, authors=None):
    approved = approvals(reviews, author, commit)
    return sorted(
        product
        for product in products_changed(files)
        if not (approved - (authors or {}).get(product, set())).intersection(
            login.lower() for login in roster.get(product, [])
        )
    )


def github(path, repository, token, data=None, raw=False):
    request = Request(
        f"https://api.github.com/repos/{repository}/{path}",
        data=json.dumps(data).encode() if data is not None else None,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.raw+json" if raw else "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def series_authors(changed, pull, repository, token):
    """Only declared authors are detectable; undeclared writers need human verification."""
    directories = {
        "/".join(parts[:3])
        for entry in changed
        for filename in (entry["filename"], entry.get("previous_filename", entry["filename"]))
        if len(parts := filename.split("/")) >= 4 and parts[0] == "content"
    }
    excluded = {}
    for directory in sorted(directories):
        required = {
            path.stem for entry in changed
            if (entry.get("status") in {"added", "modified", "copied"}
                or entry.get("status") == "renamed" and entry.get("changes", 0) > 0)
            and (path := Path(entry["filename"])).parent.as_posix() == directory
            and path.suffix == ".md" and path.name not in {"SOURCES.md", "README.md"}
        }
        endpoint = f"contents/{quote(directory + '/series.json', safe='/')}?ref="
        try:
            manifest = github(endpoint + pull["head"]["sha"], repository, token, raw=True)
        except HTTPError as error:
            if error.code != 404 or required:
                raise
            try:
                manifest = github(endpoint + pull["base"]["sha"], repository, token, raw=True)
            except HTTPError as error:
                if error.code != 404:
                    raise
                manifest = {"articles": []}
        if not isinstance(manifest, dict) or not isinstance(manifest.get("articles"), list):
            raise ValueError(f"Invalid series manifest in {directory}: articles must be a list")
        for article in manifest["articles"]:
            if not isinstance(article, dict):
                raise ValueError(f"Invalid article entry in {directory}")
            slug = article.get("slug")
            if not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
                raise ValueError(f"Invalid article slug in {directory}")
            authors = article.get("authors", [])
            if not isinstance(authors, list) or any(
                not isinstance(login, str) or not login or login != login.strip() for login in authors
            ):
                raise ValueError(f"Invalid author declaration in {directory}")
            excluded.setdefault(directory.split("/")[1], set()).update(login.lower() for login in authors)
            if authors:
                required.discard(slug)
        if required:
            raise ValueError(f"Missing authors for changed articles in {directory}: {sorted(required)}")
    return excluded


def github_pages(path, repository, token):
    result = []
    page = 1
    while True:
        separator = "&" if "?" in path else "?"
        batch = github(f"{path}{separator}per_page=100&page={page}", repository, token)
        if not isinstance(batch, list):
            raise ValueError("Unexpected GitHub API response")
        result.extend(batch)
        if len(batch) < 100:
            return result
        page += 1


def check_pull(number, repository, token, roster):
    pull = github(f"pulls/{number}", repository, token)
    if pull["state"] != "open":
        return
    commit = pull["head"]["sha"]
    github(f"statuses/{commit}", repository, token, {
        "state": "pending", "context": "industry-review",
        "description": "Checking designated industry approval for the current revision",
    })
    changed = github_pages(f"pulls/{number}/files", repository, token)
    if len(changed) != pull["changed_files"]:
        raise ValueError("Incomplete changed-file list; review fails closed")
    files = []
    for entry in changed:
        files.append(entry["filename"])
        if "previous_filename" in entry:
            files.append(entry["previous_filename"])
    reviews = github_pages(f"pulls/{number}/reviews", repository, token)
    try:
        authors = series_authors(changed, pull, repository, token)
        missing = missing_reviews(files, reviews, roster, pull["user"]["login"], commit, authors)
        blocked = bool(missing)
        description = "Industry approval missing: " + ", ".join(missing) if missing else "Industry review policy satisfied"
    except ValueError as error:
        blocked = True
        description = str(error)
    current = github(f"pulls/{number}", repository, token)
    if current["state"] != "open" or current["head"]["sha"] != commit:
        print(f"PR #{number}: head changed or PR closed; skipping stale review result")
        return
    github(f"statuses/{commit}", repository, token, {
        "state": "failure" if blocked else "success",
        "context": "industry-review",
        "description": description[:140],
    })
    if blocked:
        print(f"PR #{number}: {description}; configure the base-branch product roster and "
              "obtain a non-author human approval at the current head.")
    else:
        print(f"PR #{number}: {description}")


def main():
    event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
    repository = os.environ["GITHUB_REPOSITORY"]
    token = os.environ["GH_TOKEN"]
    roster = json.loads((ROOT / "config/reviewers.json").read_text())
    if pull := event.get("pull_request"):
        numbers = [pull["number"]]
    else:
        numbers = [pull["number"] for pull in event["workflow_run"].get("pull_requests", [])]
        if not numbers:
            numbers = [pull["number"] for pull in github_pages("pulls?state=open", repository, token)]
    failed = False
    for number in numbers:
        try:
            check_pull(number, repository, token, roster)
        except (HTTPError, ValueError) as error:
            print(f"PR #{number}: review could not complete: {error}", file=sys.stderr)
            failed = True
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
