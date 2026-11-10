# 待审证据记录：一个环，怎么把某个波长接下来？

状态：技术、逐图来源和授权待人审。作者 GitHub 账号尚未提供，`authors` 留空，不得据此安排作者自审。原稿只做待审标识和目录适配，未重新求解或核验数值。

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
| `figures/05-ring-geometry.png` | 图 1：两条总线夹一个环。上边是输入与直通，下边是下载口；耦合间隙只有 100 nm。结构示意，按 Notebook 参数绘制。 |
| `figures/16-ring-spectra.png` | 图 2：一个环给出的两条互补谱线。drop 的峰正对 through 的谷，峰间距就是 FSR。本次求解，3D FDTD，1500–1600 nm，1001 个频点。 |
| `figures/17-ring-q.png` | 图 3：把最靠近 1550 nm 的那个峰放大，半高处量出 FWHM，就得到 Q。本次求解，同一组数据的局部放大。 |
| `figures/18-ring-field.png` | 图 4：1550 nm 非谐振点的 ／Hz／，z=0 平面。最近的 drop 峰在 1546.9 nm；本图不能用于证明谐振时的能量下载。 |
| `video/ring-add-drop-GUI-3D-crop.gif` | 动画：本次 FDTD add-drop 微环的 GUI 原生 3D Carpet 动图，field 监视器，XY 平面 z = 0，Re(Hz)，λ = 1550 nm。采用已有场监视器的单频采样，展示相位变化；起伏表示场值，不是结构形变或真实脉冲传播，也不表示谐振建立的时间过程。 |
| `figures/04-fsr.png` | 图 5：同一个环的不同谐振级次。通道中心跨度、线宽、保护带及总输入光谱需一起核查，不能用 N×间隔给出必然混叠条件。教学示意。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`eb64f5d6cca2ce6f4b4cb4c84ae6402afa8ba431a84f79301eea162f574d7de5`。
