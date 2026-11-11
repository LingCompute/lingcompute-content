# 待审证据记录：间隙 50 nm 的环耦合区：怎样区分耦合与反射

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
| `figures/06-coupling-geometry.png` | 图 1：耦合区是两条波导靠近的那一小段。间隙决定倏逝场重叠的强弱，耦合长度决定累积多少。结构示意，按 Notebook 参数绘制。 |
| `figures/14-kappa-gap.png` | 图 2：κ 随间隙指数下降，100 nm 附近最敏感。教学示意，按指数衰减模型绘制，不是本次扫描。 |
| `figures/19-coupling-boundary.png` | 图 2：同一几何只改 y+ 边界，比较 through 和源端 reflection 的反向基模功率。3D FDTD，1500–1600 nm。 |
| `video/ring-coupling-pml-GUI-3D-crop.gif` | 动画：本次 FDTD 环耦合区的 PML 边界模型，GUI 原生 3D Carpet 动图，XY 平面 z = 0，Re(Hz)，λ = 1550 nm。展示已存频域场的相位变化，不是真实脉冲传播或谐振建立过程；模型为截断环段。 |
| `video/ring-coupling-absorber-GUI-3D-crop.gif` | 动画：本次 FDTD 同一环耦合区的 Absorber 边界模型，GUI 原生 3D Carpet 动图，XY 平面 z = 0，Re(Hz)，λ = 1550 nm。起伏表示场值，不代表结构形变；微弱背反射的差异须由端口读数确认，不能按两幅动图的亮度或高度判断。 |
| `figures/20-coupling-drop.png` | 图 3：PML 模型的局部 drop 正向、环段逆向和源端反射。功率均相对输入模式源归一，端口分别标明。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`706b5534b78ed6a9cd827e1822d73f19b35c1f09e7bb918f38679fc03464cafe`。
