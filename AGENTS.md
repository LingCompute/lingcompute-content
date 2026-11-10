# 协作入口

- 文章变更：先读 `docs/editorial.md`；每篇 Markdown 与随文图同属发布源稿，更新 `series.json` 与 `SOURCES.md` 后构建。
- 人审、合并或审核名单变更：先读 `docs/review.md`；由人工确认专业资格，AI 只准备稿件与检查，不作业内批准。
- 引入素材或制作材料：先读 `docs/rights.md` 与 `production/README.md`，逐项说明来源和授权。
- 工具修改：运行 `python -m unittest discover -s tests`、`python tools/build.py --check` 和完整构建；检查生成的手机截图。纯排版修改仍需视觉验收。
- `build/` 为生成物；`content/` 中待审内容通过 PR 提交。合并和公众号发送由人确认。
