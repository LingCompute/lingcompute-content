# 待审证据记录：一个环，怎么把某个波长接下来？

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/RingResonator
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/WaveguideToRingCoupling
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/BraggGratings
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/PCMBraggGratingFilter

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

环的 Q、FSR 与带宽保留取样口径；耦合功率和反射分别统计。相变两相为 EME，不是三维 FDTD，数值底限不等于实测消光比。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/05-ring-geometry.svg` | 图 1：两条总线夹一个环。上边是输入与直通，下边是下载口；耦合间隙只有 100 nm。结构示意，按 Notebook 参数绘制。 |
| `figures/16-ring-spectra.svg` | 图 2：一个环给出的两条互补谱线。drop 的峰正对 through 的谷，峰间距就是 FSR。本次求解，3D FDTD，1500–1600 nm，1001 个频点。 |
| `figures/17-ring-q.svg` | 图 3：把最靠近 1550 nm 的那个峰放大，半高处量出 FWHM，就得到 Q。本次求解，同一组数据的局部放大。 |
| `figures/18-ring-field.png` | 图 4：1550 nm 非谐振点的 ／Hz／，z=0 平面。最近的 drop 峰在 1546.9 nm；本图不能用于证明谐振时的能量下载。 |
| `video/ring-add-drop-GUI-3D-crop.gif` | 动画：本次 FDTD add-drop 微环的 GUI 原生 3D Carpet 动图，field 监视器，XY 平面 z = 0，Re(Hz)，λ = 1550 nm。采用已有场监视器的单频采样，展示相位变化；起伏表示场值，不是结构形变或真实脉冲传播，也不表示谐振建立的时间过程。 |
| `figures/04-fsr.svg` | 图 5：同一个环的不同谐振级次。通道中心跨度、线宽、保护带及总输入光谱需一起核查，不能用 N×间隔给出必然混叠条件。教学示意。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`eb64f5d6cca2ce6f4b4cb4c84ae6402afa8ba431a84f79301eea162f574d7de5`。

排版更正（2026-11-11）：将 1 个独立公式段标记为 `p.eq`，供统一排版与公式阅读计时；数学内容、数值和上下标不变，待审状态不变。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/05-ring-geometry.svg` | `b79000ecd60b3802653c7277ba8b7ce808b12ec1c5869ce0f595879fb3e9f3e3` | `44ba1fc8d2945ea2501def92c27fb2eb4f0fd5620d3c3601c81e1ac1c17e5d68` |
| `figures/16-ring-spectra.svg` | `50e64f3e80afde6a81d77d8b75e13f66635e38ba11617c63e729e24dab7ca84b` | `efc37878be8457a3b089f3a4d2c0e4ddee07023434f76014aafe26722c1a9650` |
| `figures/17-ring-q.svg` | `e96afe2d4dd466a297f517a38186a8769e249670e66f897c8ddff2b1266a03c4` | `1b07ce777627a02ed0b894cebc7096f11af27a499459aff229e2346e4b34213c` |
| `figures/04-fsr.svg` | `658cadfacd7efedaf622ef086e3105f4d11eee48689459c5aa3493cbe9634543` | `be57a7204b297a3fbb8fe45416a3a02595ad2b29029ba0dda45b24ccdcd7f0d0` |

以下原生场图、采样结构图或 GUI 动画保留栅格格式；不把 PNG/GIF 嵌入 SVG 充当可编辑矢量图：

- `figures/18-ring-field.png`
- `video/ring-add-drop-GUI-3D-crop.gif`

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
