# HTML 阅读与预览

- [正式 HTML 首页](https://lingcompute.github.io/lingcompute-content/)：只收录 `main` 中的文章。
- [待审 PR 目录](https://lingcompute.github.io/lingcompute-content/previews/)：开放 PR 的稿件快照，不代表业内审核通过。
- PR 检查列表的 **html-preview → Details** 直接打开该提交的 HTML 目录，每篇附手机长图和 Markdown 源稿。

人继续维护 Markdown、随文图片、`series.json` 与 `SOURCES.md`。新建、更新、关闭 PR，以及更新 `main` 时，`HTML previews` 工作流重新生成全站。现有开放 PR 也会被纳入，不依赖其分支上是否已有新工作流。仓库 Actions 中可手动运行该工作流补建。

预览按 `/previews/<PR号>/<完整head SHA>/` 保存，页首同时显示源稿和排版工具的提交 SHA。页面按 GitHub 中此 PR 的实际文件差异，优先列出正文变更，再列出受随文图、`series.json`、`SOURCES.md` 或内容公共文件影响的关联文章，并说明删除或移走的文章。目录可展开查看内容文件改动范围；即使该分支落后于主分支，也不会把主分支后来增加的文章当作本 PR 的删除。手机长图采用390×844参考视口；正文、长文提示、字体、图片和阅读时长复用现有生成器。公开页面不执行 JavaScript。系统字体优先，MiSans 备用；手机实际字体和公众号过滤结果仍需真机验收。

正式目录只来自主分支。预览目录加 `noindex`，但仍是公开网页，不能当作访问控制。关闭或更新 PR 后，旧快照会在下一次成功部署时移除，旧链接可能返回404。审核仍绑定 GitHub 当前提交；`html-preview` 成功仅说明预览已上线，不替代 `industry-review`。

## 本地保存即预览

首次按 README 安装依赖、Chromium 并准备字体，然后在仓库根目录运行：

```sh
python tools/dev.py
```

点击终端输出的 `http://127.0.0.1:8000/`。服务器直接读取本地工作区，未提交和新增文件也会参与；不访问 GitHub，不会自动提交或上传稿件。新建文章需同时满足 `series.json` 和来源要求。正文、随文图、`SOURCES.md`、`series.json`、产品配置、品牌签名和 CSS 保存后自动重建，已打开的浏览器自动刷新。端口被占用时运行 `python tools/dev.py --port 8001`；Ctrl+C 停止。

页面明确标注“本地实时预览 · 未提交工作区”，源稿链接打开当前本地文件。出错时页面提示具体原因并保留上次成功结果，修复保存后自动恢复。网页使用与在线预览相同的排版和篇幅测量；为缩短保存后的等待，本地监听模式不逐次生成手机长图及公众号材料，提交前仍运行完整构建。修改 Python 工具代码后需重启服务。

链接仅在本机有效，服务只监听 `127.0.0.1`，公开审阅使用提交 PR 后生成的链接。本地服务只提供生成页面、随文资源和 `content/` 中允许的源文件，不提供仓库目录列表、`.git`、凭据或 `production/`。自动刷新脚本只在本地 HTTP 响应中注入，不进入公开站点、独立 HTML 或公众号产物。临时生成物及资源缓存在停止服务时清理。

## 构建与发布边界

`pull_request_target` 只执行触发时主分支的工具与依赖。PR 只提供 `content/` 下普通文件形式的 Markdown、JSON、静态 SVG 和栅格图片；SVG 经[静态子集校验](editorial.md#可编辑图片)后内联显示，共用页面字体，源文件在本地源稿入口作为纯文本提供。符号链接、子模块、可执行文件、越界路径及超过300 MiB的内容快照会被拒绝。产品配置、审核台账、品牌、样式和 Python 代码来自受信任的工具版本。PR 对这些工具或配置的修改，合并后才影响在线排版；合并前请检查该 PR 的 `Content CI` 附件。`production/` 和仓库外的制作材料不会被发布。

渲染任务只有读取权限。发布任务在另一个 runner 上接收同一次受信任构建的产物，不执行稿件分支或产物代码；它只更新生成物分支 `gh-pages`、请求 Pages 构建，并在确认部署成功后为仍开放且 SHA 未变的 PR 写 `html-preview` 状态。发布前若主分支、现有 PR 的 SHA 或关闭状态变化，放弃该次过时构建，由后续排队的全量构建刷新，或手动重跑。全量刷新可避免并发事件合并后漏掉某个 PR。

在线版把图片和带嵌入字体的 CSS 按 SHA256 共用；不生成可独立下载的字体文件，不修改字体。现有 `Content CI` 仍提供独立 HTML、公众号内联 HTML、截图及清单。`gh-pages` 只保存当前站点文件，正常提交保留 Git 历史；站点设置900 MiB构建上限，文章规模增长后再评估增量构建与历史归档。

## 初次部署和故障处理

维护者首次把生成的站点推到 `gh-pages`，在仓库 Settings → Pages 选择 **Deploy from a branch → gh-pages → /(root)**。后续发布任务显式请求 Pages 构建，不依赖机器人推送自动触发。不要把仓库根目录或制作目录设为发布源。

维护者批量检查远端正式稿与开放 PR 时，可使用已有 GitHub 登录及项目依赖：

```sh
python tools/fonts.py
python tools/preview.py build --output /tmp/lingcompute-site-new
python -m http.server 8000 --directory /tmp/lingcompute-site-new
```

这是远端站点快照构建，与前面的本地写作服务器分开。输出目录必须不存在，避免混入旧稿；它从 GitHub 读取最新主分支与开放 PR，不会包含本地未提交稿件。维护者确认站点后，可运行 `python tools/preview.py publish --output /tmp/lingcompute-site-new`；这会推送生成物、部署并更新预览状态。发布需仓库内容写入、Pages 写入及状态写入权限。

单篇待审稿校验失败会在待审目录显示错误，其他稿件照常生成；主分支构建失败则整站不发布。部署失败时上一次站点继续可读，新提交不会获得成功预览状态。查看 Actions 的 `HTML previews` 日志后重跑；预览链接的 SHA 必须与准备审核的提交相同。
