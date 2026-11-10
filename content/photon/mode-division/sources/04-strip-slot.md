# 待审证据记录：把光从硅里搬进缝里：三种条–槽转换器

状态：技术、逐图来源和授权待人审。作者 GitHub 账号尚未提供，`authors` 留空，不得据此安排作者自审。原稿只做待审标识和目录适配，未重新求解或核验数值。

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
| `figures/19-three-designs.png` | 图 19：三种转换器的版图，从上到下依次是 MMI、对称锥、非对称锥。从本次求解的仿真结构直接绘制。 |
| `figures/20-strip-spectra.png` | 图 20：三种设计在整个 C 波段的转换效率。本次求解结果。 |
| `figures/21-strip-field.png` | 图 21：MMI 与对称锥在 1550 nm 的 ／E／²。两条路径不同，最终都把场推进了缝里。本次求解结果。 |
| `video/design1-mmi-GUI-3D-crop.gif` | 动画 1：本次 FDTD MMI 条–槽转换器的 GUI 原生动图，field 监视器，XY 平面 z = 0 μm，1550 nm，Re(Ey)。3D Carpet 的起伏表示场值，播放展示单频相位变化，不是真实脉冲传播录像。 |
| `video/design2-symmetric-GUI-3D-crop.gif` | 动画 2：本次 FDTD 对称锥条–槽转换器的 GUI 原生动图，field 监视器，XY 平面 z = 0 μm，1550 nm，Re(Ey)。场波纹随相位变化，Carpet 起伏不代表结构形变。 |
| `video/design3-asymmetric-GUI-3D-crop.gif` | 动画 3：本次 FDTD 非对称锥条–槽转换器的 GUI 原生动图，field 监视器，XY 平面 z = 0 μm，1550 nm，Re(Ey)。展示同一单频场的相位循环，跨图高度不作定量比较。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`fe8e0266a17acd123e0e909b222b424258c4d0ced6c4400f1048442af51ce8f4`。
