# 待审证据记录：双层 SiN 端面耦合：薄层接光，厚层布线

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/BilayerSiNEdgeCoupler
- https://www.lingcompute.com/photon/learning-center/example-library
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/EdgeCoupler
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/WaveguideSizeConverter
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/FreeFormCoupler

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

双层 SiN 是层间模式转移，不是上下衍射相消。不同接口不能跨波段直接排名；净通量不等于 TE0。厚度—有效折射率标定的并行实现不改变物理设置。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/20-bilayer-structure.svg` | 图 1：双层的对接关系。上层负责把模场撑开，下层在 200 μm 处接手送到波导。上层画得更透明，便于看出相对位置。 |
| `figures/04-bilayer-principle.svg` | 图 2：薄上层的端面模式经重叠锥形区转移到厚下层。两层均为 SiN，图为非等比例侧视示意。 |
| `figures/21-bilayer-field.png` | 图 3：y = 0 截面的模场。光从左侧光纤进入，在上层 SiN 中逐渐被约束，到 200 μm 之后交给下层。 |
| `figures/25-bilayer-zoom.png` | 图 4：交接处的放大场图。上层在 200 μm 处开始收窄，下层同时接住模场，到 275 μm 完全交给 0.38 μm 波导。 |
| `figures/22-bilayer-spectrum.svg` | 图 5：耦合谱。450–640 nm 内都在 −4 dB 以内，但 400 nm 端明显恶化。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`c4f7f1d88cae2780e2820603dfb4d6def5663139badebfc1aac5a780d5e5e16e`。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/20-bilayer-structure.svg` | `a4321443330af86ec11ee4284d871ec6bd87387a646b1f64323edf51ca07f6cd` | `be0b986ccc8ecd2c3b3aaa4ec8df21db121791289e76003942e73425ff23a4b1` |
| `figures/04-bilayer-principle.svg` | `5ceb99271c2365dabf5ed6cd4b655ad4197a5c1186f0bc4feef863d9c7eb4f1d` | `e13f97b25151dfcca7c22ba9c021281d97c0c13290fab961f1fddc448dd0e5ad` |
| `figures/22-bilayer-spectrum.svg` | `401115a040e58de76e5ddf065f65066cd1e8018b12c959aac915275c16f0da25` | `ecb317babd4e11f482d502b8869e58edf4a26e16809728056e497a648f65c02c` |

以下原生场图、采样结构图或 GUI 动画保留栅格格式；不把 PNG/GIF 嵌入 SVG 充当可编辑矢量图：

- `figures/21-bilayer-field.png`
- `figures/25-bilayer-zoom.png`

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
