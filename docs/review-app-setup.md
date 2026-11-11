# 专用审核 App 启用步骤

本步骤由组织管理员执行一次。PR 内的工作流已经准备好，但注册 App、保管私钥和迁移仓库保护属于组织配置，不能仅靠合并代码完成。所有步骤完成前，继续保留现有保护和人工审核，不宣布行业状态身份隔离已经启用。

## 注册及安装

1. 在 LingCompute 组织的 Developer settings → GitHub Apps 创建组织自有 App，名称例如 `LingCompute content review`，主页指向本仓库，关闭 Webhook，不订阅事件。
2. Repository permissions 仅授予 Contents: Read-only、Pull requests: Read-only、Commit statuses: Read and write。Metadata 的必需读取权限由 GitHub 自动附带。不要授予仓库内容写入、管理、工作流修改或组织权限。
3. 仅安装到 `LingCompute/lingcompute-content`。记录 App 的数值 **App ID**，不要使用 Installation ID 或 OAuth Client ID 替代保护检查的来源 ID。
4. 生成私钥。它只用于后续环境 Secret；不写进 Git、PR、评论、日志或本仓库的制作材料。App 注册与安装不能由普通仓库 API 令牌代办，需具备组织设置权限的人员确认。

## 保护环境

在仓库 Settings → Environments 新建 `industry-review`：

- Deployment branches and tags 选择 Selected branches and tags，添加 **Branch: `main`**；不添加 Tag、`codex/*` 或 PR 分支。不要选择仅依据仓库所有受保护分支的模式，以免其他受保护分支取得私钥。
- 环境 Variable `INDUSTRY_REVIEW_APP_ID`：填上述 App ID。
- 环境 Secret `INDUSTRY_REVIEW_APP_PRIVATE_KEY`：填完整 PEM 私钥。它只存放在这个受保护环境，不能改成 repository/organization Secret。

维护者复核环境只允许 `main` 后，再合并已获人工批准的工作流修复 PR。工作流运行时签出默认分支，使用固定版本的 `actions/create-github-app-token`，令牌权限再次限制为上述三项。

## 迁移规定检查

工作流修复合并后，管理员在 main 的分支保护中保留 `build` 及全部人工审批要求，把 `industry-review` 的 Expected source 从 **GitHub Actions** 改为专用 App。需要先运行一次默认分支可信审核任务，让该 App 在提交上产生状态，才能在界面选择其来源。

使用 REST 配置时，现有规定检查中的这一项应为：

```json
{"context": "industry-review", "app_id": 123456}
```

将示例中的 `123456` 替换为实际专用 App ID。`build` 继续绑定 GitHub Actions（15368）；保留 strict、管理员约束、旧批准撤销、代码所有者批准、最后推送后批准、线性历史、禁止强推/删除和讨论解决要求。不要将 `app_id` 设为 `-1`，不要为解决等待状态而删除规定检查。

切换期间不合并其他文章。随后重新运行默认分支的 Industry review 任务：当前缺少作者声明或指定业内审核者的稿件应由**专用 App**写入失败状态；没有文章变更的工具 PR 可写入成功，但仍须满足原生人工审批。配置失败时修复 App/Environment，不使用 Actions 令牌兜底，也不降低保护。

## 验收

- 检查 `GET /repos/LingCompute/lingcompute-content/branches/main/protection/required_status_checks`，确认 `industry-review` 的 `app_id` 是专用 App ID，且 `build` 与 strict 保持原值。
- 检查 Environment 的部署分支策略，确认仅 Branch `main`；PR 分支不得取得私钥。
- 检查工作流的令牌步骤成功、状态来源显示为专用 App；私钥和安装令牌未出现在日志。
- 核对至少一篇缺少人审的文章继续失败。自动化成功不代表作者、审核者资格或技术内容已经审核通过。

依据：GitHub 官方 [GITHUB_TOKEN 权限](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#permissions)、[环境部署分支限制](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments)、[保护分支的规定状态来源](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-status-checks-before-merging)及 [create-github-app-token](https://github.com/actions/create-github-app-token)。
