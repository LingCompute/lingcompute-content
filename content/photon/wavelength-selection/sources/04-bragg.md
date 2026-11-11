# 待审证据记录：周期结构怎么只反射一个波长？

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
| `figures/07-bragg-geometry.svg` | 图 1：波导两侧的周期性齿。周期 Λ 与有效折射率一起决定反射哪个波长。结构示意，按 Notebook 参数绘制。 |
| `figures/08-bragg-condition.svg` | 图 2：正向模与反向模的波矢差，必须由光栅矢量补上。示意图。 |
| `figures/21-bragg-spectra.svg` | 图 3：同一周期、同一材料，只有齿的相位不同：对齐段形成深阻带，错位段几乎全透。本次求解，3D FDTD，1532 nm 附近。 |
| `figures/22-bragg-field.png` | 图 4：两条并行结构在阻带内的场：对齐齿结构透射受抑，错位齿结构主要通过。本次 Ey 实部，z=110 nm，1532 nm。 |
| `video/bragg-aligned-GUI-3D-crop.gif` | 动画：本次 FDTD 对齐与错位 Bragg 光栅的 GUI 原生 3D Carpet 动图，fields_xy 监视器，XY 平面 z = 110 nm，Re(Ey)，λ = 1532 nm。展示单频场相位变化，起伏表示场值，不是真实脉冲反射录像；反射与透射大小仍需通量监视器统计。 |
| `figures/15-kappaL.svg` | 图 5：均匀无损模型的中心抑制度 ER=20log10(cosh κL)。dB 值不会因反射率接近 1 而饱和；图为解析示意，不是本次长度扫描。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`b17a225254c7615ad0b35e63f2c020a7e063030621de82a9029acb4f27739006`。

排版更正（2026-11-11）：将 2 个独立公式段标记为 `p.eq`，供统一排版与公式阅读计时；数学内容、数值和上下标不变，待审状态不变。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/07-bragg-geometry.svg` | `ae80b6431dbff10a16ecfec984fe122509c5fdfc82ad70dda39b56f8bbaaa690` | `5e14517ca858707239004eef5478bd6c867aeb55701704aefdd67af57154d4a0` |
| `figures/08-bragg-condition.svg` | `0ef01a9c35708f4c05816ace36e89d268ed03f40faa1af163cb9848a37791468` | `a214475f11417df4e053b626a2c666f57cda962874a923f526935f3bf041ea6b` |
| `figures/21-bragg-spectra.svg` | `310f78dbc481c77eca40feaaa87840befe73d9c365f64308aa5ca62830cd81d9` | `acc28824b28209929376e4985c1eb3daf1e18f1ac977c019cd66b4f077749484` |
| `figures/15-kappaL.svg` | `50c5b4052e4229dba9decb013ef0a686137fdfebda7c39f063b47cd2a72e474d` | `23d905ab6e2def5684422a034059efe09e8b4c9e4fc9aac2a58ab6c18f15a17b` |

以下原生场图、采样结构图或 GUI 动画保留栅格格式；不把 PNG/GIF 嵌入 SVG 充当可编辑矢量图：

- `figures/22-bragg-field.png`
- `video/bragg-aligned-GUI-3D-crop.gif`

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
