# 待审证据记录：同样转 90°，Euler 弯为什么能少丢一点光？

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/EulerWaveguideBend
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/WaveguideCrossing
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/SWGWaveguideCrossing
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/ZeroCrossTalkTE

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

圆弧/Euler 与有包层/裸波导仅在配对条件下作定量比较。交叉串扰为 +y 单侧，需写清净通量还是已存导模。100 弯预算是损耗外推，不是多弯 FDTD。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/04-curvature.svg` | 图 1：圆弧的曲率出现阶跃；本例 Euler 弯两端为渐变曲线，中间接一段恒曲率圆弧。渐变的是曲率，而不只是看起来顺滑的外轮廓。 |
| `figures/08-bend-geometry.svg` | 图 2：从本次实际仿真读取的器件俯视结构。端口占位相同，但 Euler 中心线会偏离圆弧，不能按相同最小半径理解。 |
| `figures/09-bend-fields.png` | 图 3：1550 nm 的电场幅值 ／E／，两图使用相同线性色标。图像用来确认光走向哪里，微小损耗差异交给模式端口计算。 |
| `video/euler-circular-GUI-3D-crop.gif` | 动画：本次 FDTD 圆弧弯的 GUI 原生 3D Carpet 动图，XY 平面 z = 105 nm，Re(Hz)，λ = 1550 nm。Hz 垂直于布线平面，便于观察完整转向；这是单频场相位演示，不是真实脉冲传播，起伏表示场值而非结构形变。 |
| `video/euler-euler-GUI-3D-crop.gif` | 动画：本次 FDTD Euler 弯的 GUI 原生 3D Carpet 动图，XY 平面 z = 105 nm，Re(Hz)，λ = 1550 nm。图像用于观察路径与相位；微小损耗差异仍以模式端口读数为准，不能按起伏高度判断。 |
| `figures/10-bend-loss.svg` | 图 4：1500–1600 nm 的基模损耗谱。本次 Euler 曲线总体更低；中心波长读数不代表所有几何、所有波段都保持同一比例。 |
| `figures/20-loss-budget.svg` | 图 5：这是单弯读数的线性预算外推，不是含 100 个弯的 FDTD 求解；尚未计入直段损耗、反射相干叠加或器件之间的耦合。 |
| `figures/07-workflow.svg` | 图 6：先定可用空间，再分配单弯损耗上限，最后核查工艺与累计效应。选型从约束出发，比单独追求最低损耗更有用。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`ce7dd7653552540ecbe89920862fbfc763fb0bda7c614927e58d990c08f4a665`。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/04-curvature.svg` | `b8390d7442e70f2ed9137e388c3a503db04deca68d7e7ac9b100b1523940baa4` | `ecf9afdde79880751969f2a6f07e12983596842c028e5ab1a7ab80b3db1762b5` |
| `figures/08-bend-geometry.svg` | `497c2a49b543cce3e5f4491378e6b19f9c595e5a2b079aaf2588d542829b638d` | `4cefb1e202deb08352e8b73111ce0b963c4a239fa6c7b8fb999af49168d7cebc` |
| `figures/10-bend-loss.svg` | `9fd24fb394ed424900b81b3804527d7c94a5d63ce1305c79c00db0ccb8f40579` | `8229cde30b36e4f621469d2673be1e5ac21050d860503695d933909c439ef05b` |
| `figures/20-loss-budget.svg` | `0af4cc3b2997a06bf2455d49cc33830f5d9bf6c988b4c19760f7ac864bf3214c` | `649edfe248cd3c71e86ad6f26a10fd9d8934acaa52da1bb20c25abf3e11eab55` |
| `figures/07-workflow.svg` | `70e8a879998dd46503a1d9c3a3cd0f2dc841b63fafb7294ab3a89de1d79368cf` | `dedb2d073861ed1c65252f3d432109f28e0494789289059008a64c85f1756100` |

以下原生场图、采样结构图或 GUI 动画保留栅格格式；不把 PNG/GIF 嵌入 SVG 充当可编辑矢量图：

- `figures/09-bend-fields.png`
- `video/euler-circular-GUI-3D-crop.gif`
- `video/euler-euler-GUI-3D-crop.gif`

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
