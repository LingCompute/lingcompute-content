# 待审证据记录：让一束光，在宽波导里自己干涉成像

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/MMIPowerSplitter2x2
- https://www.lingcompute.com/photon/learning-center/example-library
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/YJunction
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/DirectionalCoupler

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

MMI 端口占比以两路之和归一化，总透射以输入源归一化；三类器件的材料、端口与采样条件不同，不构成同条件排名。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/06-mmi.png` | 图 1：2×2 MMI 的 FDTD 仿真场图。颜色表示频域场强 ／E／²，多模区的空间分布体现了模式间的干涉。 |
| `figures/16-mmi-phase.svg` | 图 2：解析相位示意，绘出 m = 1–4 相对基模的相位差并对 2π 取余。在 3Lπ 处奇模反相、偶模同相，得到镜像单像；在 6Lπ 处全部同相，得到同向单像。 |
| `video/MMIPowerSplitter2x2-GUI-3D-crop.gif` | 动图 1：2×2 MMI 的 3D Carpet 动画。Re(Ey)，λ = 1.55 μm；展示单频场随相位变化的分布，起伏表示场值，并非结构形变或脉冲传播。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`cba7fd7ddd3607856be7ab8bfb79454731bf7b4d415fb8312fd541ba64793579`。

排版更正（2026-11-11）：将 4 个独立公式段和 1 个数值代入段标记为 `p.eq`，供统一排版与公式阅读计时；数学内容、数值和上下标不变，待审状态不变。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/16-mmi-phase.svg` | `3393edae960b7646ff0d30dbe36528bce1636f74a65bded1588767b8f7dff432` | `1185144ca7f7af22ab66ba639f885c00bceffdded55a4f9506c9f18a324fd6ae` |

`16-mmi-phase.svg` 的标题保留本 PR 现有“走够长度，各模式的相位重新对齐”；相位盘、曲线和端口位置沿用原工程。

以下原生场图、采样结构图或 GUI 动画保留栅格格式；不把 PNG/GIF 嵌入 SVG 充当可编辑矢量图：

- `figures/06-mmi.png`
- `video/MMIPowerSplitter2x2-GUI-3D-crop.gif`

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
