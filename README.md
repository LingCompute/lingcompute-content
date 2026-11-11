<img src="assets/brand/lingcompute-horizontal.svg" alt="灵算科技 LingCompute" width="300">

# 灵算技术内容库

面向工程师、科研人员和学习者的灵算官方技术内容。按产品和系列阅读，每篇说明读者前提、原理、证据和适用条件。

**[打开 HTML 阅读版](https://lingcompute.github.io/lingcompute-content/)** · [查看待审 PR 预览](https://lingcompute.github.io/lingcompute-content/previews/)

## 按产品阅读

<!-- BEGIN GENERATED CATALOG -->

| 产品 | 系列 | 产品入口 |
| --- | --- | --- |
| 灵算光子 | [图解无源光子器件 · 功率分配](#series-photon-power-splitters)、[图解无源光子器件 · 波分解复用](#series-photon-wdm-demultiplexing) | [产品介绍](https://www.lingcompute.com/products/photon) |
| 灵算流体 | 待首篇审核后收录 | [产品介绍](https://www.lingcompute.com/products/fluid) |
| 灵算射频 | 待首篇审核后收录 | [产品介绍](https://www.lingcompute.com/products/rf) |
| 灵算洞察 | 待首篇审核后收录 | [产品介绍](https://www.lingcompute.com/products/insight) |

<a id="series-photon-power-splitters"></a>

### 图解无源光子器件 · 功率分配

适合：具有光学基础、需要理解和选择集成光子器件的工程师与科研人员。

1. [一束光，怎么被“掰”成两路？](content/photon/power-splitters/01-y-junction.md) — 区分分光比和总透射，理解对称Y分支如何实现宽带等分。

   预计阅读 **6–11 分钟**，实操另计。 [来源、定量口径与素材说明](content/photon/power-splitters/SOURCES.md)。

2. [两条波导靠得够近，光就自己换手](content/photon/power-splitters/02-directional-coupler.md) — 从超模相位和耦合模模型出发，理解功率交换及长度、失配和几何参数的取舍。

   预计阅读 **14–26 分钟**，实操另计。 **长文提示：超过10参考屏，建议先扫描小标题，再按问题细读。** [来源、定量口径与素材说明](content/photon/power-splitters/SOURCES.md)。


<a id="series-photon-wdm-demultiplexing"></a>

### 图解无源光子器件 · 波分解复用

适合：具有光学基础、需要理解和选择集成光子器件的工程师与科研人员。

1. [分波器怎么选：五条约束的联立](content/photon/wdm-demultiplexing/05-comparison.md) — 按通道、带宽、串扰、面积和工艺联合选择分波方案。

   预计阅读 **5–8 分钟**，实操另计。 [来源、定量口径与素材说明](content/photon/wdm-demultiplexing/SOURCES.md)。

阅读时长为编辑模型估计；参考视口为390×844 CSS像素，不同设备会有差异。

<!-- END GENERATED CATALOG -->

两篇功率分配历史稿的当前版本已由项目负责人确认完成历史人审；审核者署名和实际日期未提供，记录见 [legacy.json](reviews/legacy.json)。后续篇目通过独立 PR 审核后逐篇收录。公开 PR 中的稿件仍是待审稿；分支目录用于预览该分支，正式目录以 `main` 为准，收录也不等于已经在公众号发送。

## 投稿与生成

人维护 Markdown 和随文素材；工具生成 HTML、手机截图、阅读时长和上传清单。技术结论由指定业内审核者审批，微信公众号最终发送由人操作。

新制或重绘的技术插图以可编辑 SVG 随文维护，保留文字和矢量对象。HTML 预览直接显示 SVG，公众号构建自动导出 PNG 上传副本；源图规则见[可编辑图片](docs/editorial.md#可编辑图片)。

写作时运行 `python tools/dev.py`，打开终端输出的本地链接（默认 `http://127.0.0.1:8000/`）。保存正文、图片、来源、系列信息或 CSS 后自动重建并刷新；未提交和新增文件也会参与预览，无需 GitHub 登录。首次使用先完成下面的依赖、Chromium 与字体准备。完整命令和故障说明见 [实时预览](docs/previews.md#本地保存即预览)。

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
python -m unittest discover -s tests
python tools/build.py --check
python tools/fonts.py
python tools/build.py
python tools/catalog.py
```

在线审阅优先打开 PR 检查列表中的 **html-preview → Details**，直接查看当前提交的 HTML 与手机长图；主分支文章见 [HTML 阅读版](https://lingcompute.github.io/lingcompute-content/)。流程及版本边界见 [HTML 预览说明](docs/previews.md)。

本地可打开生成的 `build/index.html`。CI 的 `article-preview` 附件继续提供独立 HTML、公众号排版材料及清单；下载后可离线查看。生成物只由发布任务更新 `gh-pages`，不提交到源稿分支。投稿方式见 [CONTRIBUTING.md](CONTRIBUTING.md)，默认排版与篇幅见 [编辑规范](docs/editorial.md)，审核流程见 [审核规则](docs/review.md)。

首页标记区由 `series.json`、当前源稿和构建报告生成，提供读者前提、文章问题、预计阅读时长及长文提示。增删文章或修改正文、随文图后，重新构建并运行 `python tools/catalog.py`，将 README 更新随同一 PR 提交；CI 用 `python tools/catalog.py --check` 拦截遗漏或过期信息。

默认使用设备的系统字体：先匹配系统界面字体（`system-ui`、`-apple-system`、`BlinkMacSystemFont`），中文依次匹配苹方、冬青黑体、微软雅黑、Noto Sans CJK SC；随后回退到小米 MiSans，最后使用通用无衬线字体。正文采用常规字重（400）、小标题及表头采用中等字重（500）、标题及强调采用半粗字重（600）；MiSans 对应使用 Regular、Medium、Semibold。`tools/fonts.py` 首次从[小米官方](https://hyperos.mi.com/font/en/download/)下载约 228 MB 字体包，仅在本机缓存三份未经修改、经 SHA256 校验的原始 WOFF2；后续复用缓存。备用字体嵌入独立 HTML 预览，不单独随仓库或 CI 附件分发。GitHub Markdown 的字体由 GitHub 控制；公众号编辑器可能过滤字体设置，发送前需真机检查。详见[字体与授权](docs/rights.md#字体)。

| 目录 | 用途 |
| --- | --- |
| `content/<产品>/<系列>/` | Markdown、随文图与最小证据记录；主分支只收录已审内容 |
| `production/` | 投稿者可选择附带的制作材料，独立于文章审核 |
| `tools/`、`tests/` | 共享生成、检查与测试 |
| `assets/brand/` | 公司标识及单独的商标说明 |
| `build/` | 自动生成的预览和公众号排版材料 |

自有工具代码采用 [MIT](LICENSE)，自有文章和插图采用 [CC BY-NC 4.0](LICENSE-CONTENT.md)，允许署名的非商业转载和改编，商业使用另行授权。商标、产品界面及另有标注的第三方材料按[各自权利说明](docs/rights.md)处理。来源页面和产品功能可能更新，请以当前官方文档为准。
