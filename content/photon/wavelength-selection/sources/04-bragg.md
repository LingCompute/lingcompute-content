# 待审证据记录：周期结构怎么只反射一个波长？

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
| `figures/07-bragg-geometry.png` | 图 1：波导两侧的周期性齿。周期 Λ 与有效折射率一起决定反射哪个波长。结构示意，按 Notebook 参数绘制。 |
| `figures/08-bragg-condition.png` | 图 2：正向模与反向模的波矢差，必须由光栅矢量补上。示意图。 |
| `figures/21-bragg-spectra.png` | 图 3：同一周期、同一材料，只有齿的相位不同：对齐段形成深阻带，错位段几乎全透。本次求解，3D FDTD，1532 nm 附近。 |
| `figures/22-bragg-field.png` | 图 4：两条并行结构在阻带内的场：对齐齿结构透射受抑，错位齿结构主要通过。本次 Ey 实部，z=110 nm，1532 nm。 |
| `video/bragg-aligned-GUI-3D-crop.gif` | 动画：本次 FDTD 对齐与错位 Bragg 光栅的 GUI 原生 3D Carpet 动图，fields_xy 监视器，XY 平面 z = 110 nm，Re(Ey)，λ = 1532 nm。展示单频场相位变化，起伏表示场值，不是真实脉冲反射录像；反射与透射大小仍需通量监视器统计。 |
| `figures/15-kappaL.png` | 图 5：均匀无损模型的中心抑制度 ER=20log10(cosh κL)。dB 值不会因反射率接近 1 而饱和；图为解析示意，不是本次长度扫描。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`b17a225254c7615ad0b35e63f2c020a7e063030621de82a9029acb4f27739006`。

排版更正（2026-11-11）：将 2 个独立公式段标记为 `p.eq`，供统一排版与公式阅读计时；数学内容、数值和上下标不变，待审状态不变。
