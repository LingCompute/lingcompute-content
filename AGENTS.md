# 协作入口

- 文章变更：先读 `docs/editorial.md`；每篇 Markdown 与随文图同属发布源稿，更新 `series.json` 与 `SOURCES.md` 后构建。
- 人审、合并或审核名单变更：先读 `docs/review.md`；由人工确认专业资格，AI 只准备稿件与检查，不作业内批准。
- 引入素材或制作材料：先读 `docs/rights.md` 与 `production/README.md`，逐项说明来源和授权。
- 工具修改：运行 `python -m unittest discover -s tests`、`python tools/build.py --check` 和完整构建；检查生成的手机截图。纯排版修改仍需视觉验收。
- 合并权限：先读 `docs/review.md`；非 `content/` 维护 PR 通过必需检查后可由维护者自行合并；涉及 `content/` 的 PR 须由非作者的指定业内审核者批准当前提交。公众号发送由人确认。
- `build/` 为生成物，源稿与维护改动均通过 PR 提交。
