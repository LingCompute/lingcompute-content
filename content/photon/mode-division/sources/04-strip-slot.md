# 待审证据记录：把光从硅里搬进缝里：三种条–槽转换器

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/8ChannelDemultiplexer
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/Autograd3InverseDesign
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/StripToSlotConverters

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

模式纯度的分母是已存导模之和，不等于输入功率。八通道器件只验证 I3/I7 两个入口，耦合长度来自文献而非本次优化。逆向设计目标函数不等于器件效率。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/18-slot-mode.png` | 图 18：左为条波导，场关在硅里；右为槽波导，场被挤进中间 100 nm 的缝。本地模式求解。 |
| `figures/19-three-designs.svg` | 图 19：三种转换器的版图，从上到下依次是 MMI、对称锥、非对称锥。从本次求解的仿真结构直接绘制。 |
| `figures/20-strip-spectra.svg` | 图 20：三种设计在整个 C 波段的转换效率。本次求解结果。 |
| `figures/21-strip-field.png` | 图 21：MMI 与对称锥在 1550 nm 的 ／E／²。两条路径不同，最终都把场推进了缝里。本次求解结果。 |
| `video/design1-mmi-GUI-3D-crop.gif` | 动画 1：本次 FDTD MMI 条–槽转换器的 GUI 原生动图，field 监视器，XY 平面 z = 0 μm，1550 nm，Re(Ey)。3D Carpet 的起伏表示场值，播放展示单频相位变化，不是真实脉冲传播录像。 |
| `video/design2-symmetric-GUI-3D-crop.gif` | 动画 2：本次 FDTD 对称锥条–槽转换器的 GUI 原生动图，field 监视器，XY 平面 z = 0 μm，1550 nm，Re(Ey)。场波纹随相位变化，Carpet 起伏不代表结构形变。 |
| `video/design3-asymmetric-GUI-3D-crop.gif` | 动画 3：本次 FDTD 非对称锥条–槽转换器的 GUI 原生动图，field 监视器，XY 平面 z = 0 μm，1550 nm，Re(Ey)。展示同一单频场的相位循环，跨图高度不作定量比较。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`fe8e0266a17acd123e0e909b222b424258c4d0ced6c4400f1048442af51ce8f4`。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/19-three-designs.svg` | `ffc6e2d48fababc84524462ed96b4ae184127d613d684415fc8223b782772230` | `7e1797744212ede6d5d0ceeb719eae41b2dbfff538e4ceaf3b4b2bb3fb9c4131` |
| `figures/20-strip-spectra.svg` | `24e6c8c73ea4fdfee5b230582d3d0653e0ee8f5d330ab5cbb16cbb5b19483b31` | `d66fc12d5aafacc19db3780f91d424cc48c54fb0c725dbdfb01bb7ec29b145e2` |

以下原生场图、采样结构图或 GUI 动画保留栅格格式；不把 PNG/GIF 嵌入 SVG 充当可编辑矢量图：

- `figures/18-slot-mode.png`
- `figures/21-strip-field.png`
- `video/design1-mmi-GUI-3D-crop.gif`
- `video/design2-symmetric-GUI-3D-crop.gif`
- `video/design3-asymmetric-GUI-3D-crop.gif`

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
