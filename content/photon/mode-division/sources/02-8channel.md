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
| `figures/06-device-layout.png` | 图 6：整器件版图，八条入口波导在约 200 μm 内逐级并入中央总线。从本次求解的仿真结构直接绘制。 |
| `figures/07-coupler-geometry.png` | 图 7：TE0→TE3 耦合器的几何。耦合长度 17.6 μm，间隙 200 nm。真实多边形，非示意。 |
| `figures/08-coupler-spectra.png` | 图 8：六个耦合器的总透射谱。TE 三档在 95% 以上，TM 三档略低。本次求解结果。 |
| `figures/09-mode-fraction.png` | 图 9：目标模式占比。整条 C 波段都在 99% 以上。本次求解结果。 |
| `figures/10-coupler-field.png` | 图 10：TE0→TE3 耦合器在 1550 nm 的 ／E／²（dB，相对峰值）。耦合区走完，能量已从窄波导转到宽波导的高阶模上。本次求解结果。 |
| `video/coupler-te3-GUI-3D-crop.gif` | 动画 1：本次 FDTD TE0→TE3 单段耦合器的 GUI 原生动图，field 监视器，XY 平面 z = 0 μm，1550 nm，Re(Ey)。3D Carpet 的起伏表示场值，播放为单频场的相位变化，不是真实脉冲传播录像。 |
| `figures/11-device-field.png` | 图 11：整器件在两个入口下的 ／E／²。上图 I3 注 TE0，下图 I7 注 TM0。本次求解结果。 |
| `video/device-i3-GUI-3D-crop.gif` | 动画 2：本次 FDTD 整器件 I3 入口的 GUI 原生动图，field 监视器，XY 平面 z = 0 μm，1550 nm，Re(Ey)。仅展示 I3 注入 TE0 的这条路径，不能据此声称八个入口均已验证；播放为单频相位演示。 |
| `video/device-i7-GUI-3D-crop.gif` | 动画 3：本次 FDTD 整器件 I7 入口的 GUI 原生动图，field 监视器，XY 平面 z = 0 μm，1550 nm，Re(Ez)。该 TM 激励在此平面的 Ey 为零，因此选用 Ez。Carpet 起伏表示场值，不代表结构形变，跨图高度不作定量比较。 |
| `figures/12-coupling-length.png` | 图 12：六个耦合器的长度对比。TM 族明显更短，说明它的模式重叠更强。文献值，本次未扫描。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`99b5b6ce51bb4640b005fced88953be655390f7fad9cb6c8eab8865e13bf3ffb`。
