# 待审证据记录：两个介质抛物面，怎样连接两根波导

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/FreeFormCoupler
- https://www.lingcompute.com/photon/learning-center/example-library
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/EdgeCoupler
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/BilayerSiNEdgeCoupler
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/WaveguideSizeConverter

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

双层 SiN 是层间模式转移，不是上下衍射相消。不同接口不能跨波段直接排名；净通量不等于 TE0。厚度—有效折射率标定的并行实现不改变物理设置。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/15-ffc-geometry.png` | 图 1：自由曲面耦合器的结构与光路。输入波导的发散光打到抛物面上，反射并聚焦到对面波导。 |
| `figures/06-mirror-principle.png` | 图 2：抛物面把「耦合」变成了「成像」。发散的光被准直、再被聚焦。 |
| `figures/17-ffc-spectrum.png` | 图 3：耦合谱。400 nm 带宽内都在 −1.2 dB 以内，谱线朝短波侧略高。 |
| `figures/16-ffc-field.png` | 图 4：3 μm 偏移下的场分布。左侧波导出射后发散，经抛物面反射在右侧重新汇聚。 |
| `video/ffc-3um-GUI-3D-crop.gif` | 动画 1：本次 FDTD 自由曲面耦合器的 GUI 原生场动画，field 监视器，XY 平面 z = 0 μm，850 nm，Re(Ez)。3D Carpet 的起伏表示场值，展示单频场的相位变化，不是真实脉冲飞行或反射录像。 |
| `figures/26-ffc-sections.png` | 图 5：入口与出口的横向场剖面。入口是波导内的紧凑模场，出口已经展宽到接近波导宽度。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`8dcc3ff513594045dff6ba2968448864dd764d9ce4c5fdb5d9eb9aafd7d0494e`。
