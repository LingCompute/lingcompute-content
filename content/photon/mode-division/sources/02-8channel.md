# 待审证据记录：八个入口，一根总线：模分复用器怎么装配

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
| `figures/06-device-layout.svg` | 图 6：整器件版图，八条入口波导在约 200 μm 内逐级并入中央总线。从本次求解的仿真结构直接绘制。 |
| `figures/07-coupler-geometry.svg` | 图 7：TE0→TE3 耦合器的几何。耦合长度 17.6 μm，间隙 200 nm。真实多边形，非示意。 |
| `figures/08-coupler-spectra.svg` | 图 8：六个耦合器的总透射谱。TE 三档在 95% 以上，TM 三档略低。本次求解结果。 |
| `figures/09-mode-fraction.svg` | 图 9：目标模式占比。整条 C 波段都在 99% 以上。本次求解结果。 |
| `figures/10-coupler-field.png` | 图 10：TE0→TE3 耦合器在 1550 nm 的 ／E／²（dB，相对峰值）。耦合区走完，能量已从窄波导转到宽波导的高阶模上。本次求解结果。 |
| `video/coupler-te3-GUI-3D-crop.gif` | 动画 1：本次 FDTD TE0→TE3 单段耦合器的 GUI 原生动图，field 监视器，XY 平面 z = 0 μm，1550 nm，Re(Ey)。3D Carpet 的起伏表示场值，播放为单频场的相位变化，不是真实脉冲传播录像。 |
| `figures/11-device-field.png` | 图 11：整器件在两个入口下的 ／E／²。上图 I3 注 TE0，下图 I7 注 TM0。本次求解结果。 |
| `video/device-i3-GUI-3D-crop.gif` | 动画 2：本次 FDTD 整器件 I3 入口的 GUI 原生动图，field 监视器，XY 平面 z = 0 μm，1550 nm，Re(Ey)。仅展示 I3 注入 TE0 的这条路径，不能据此声称八个入口均已验证；播放为单频相位演示。 |
| `video/device-i7-GUI-3D-crop.gif` | 动画 3：本次 FDTD 整器件 I7 入口的 GUI 原生动图，field 监视器，XY 平面 z = 0 μm，1550 nm，Re(Ez)。该 TM 激励在此平面的 Ey 为零，因此选用 Ez。Carpet 起伏表示场值，不代表结构形变，跨图高度不作定量比较。 |
| `figures/12-coupling-length.svg` | 图 12：六个耦合器的长度对比。TM 族明显更短，说明它的模式重叠更强。文献值，本次未扫描。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`99b5b6ce51bb4640b005fced88953be655390f7fad9cb6c8eab8865e13bf3ffb`。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/06-device-layout.svg` | `f33769c2e7bc374237e00e0168b18dd6ccab3e7fe37c9c699cea52510e879ffa` | `908e43840494912dcdaaf07cd2be536c6e5a50c56259083748320c661070ff6e` |
| `figures/07-coupler-geometry.svg` | `a2c6b6ea9440fe7edb22c3e59bef15e06b741a7aa41e5009b1e740bd502bbada` | `9ffa72d84c978bfffaee89226ff2dc902bd283e4b5ed3552de1df4eb8f036aee` |
| `figures/08-coupler-spectra.svg` | `e4638a8cbd79af7a81ae9ba83523912ff4f7354856ff9de4f0f98cc22afe7320` | `687b75d637a48163c642f354b966aa71531b5e80cc3910d14915cb453c1b30d2` |
| `figures/09-mode-fraction.svg` | `162910be2f6a2acd98509e0057c8444b110d5b16992581417cd3979ddb8f2fb0` | `a50695538b473b753b143034075e34032653179a3c54e27d9cd3c9fdbbcff592` |
| `figures/12-coupling-length.svg` | `42e0f1bd40fd1a2da844bbdeeef7a1138b8eb8bedab49adfacccbdfb4853850f` | `c3706d8fb5855c0699098b78b83ca1f883eba946e3f0c875d795ee61c8f21a25` |

以下原生场图、采样结构图或 GUI 动画保留栅格格式；不把 PNG/GIF 嵌入 SVG 充当可编辑矢量图：

- `figures/10-coupler-field.png`
- `video/coupler-te3-GUI-3D-crop.gif`
- `figures/11-device-field.png`
- `video/device-i3-GUI-3D-crop.gif`
- `video/device-i7-GUI-3D-crop.gif`

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
