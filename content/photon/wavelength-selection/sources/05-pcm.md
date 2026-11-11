# 待审证据记录：同一块材料，怎么让阻带搬家？

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
| `figures/09-pcm-structure.png` | 图 1：Si 波导上周期排布 Sb2Se3 块。晶态折射率 4.16，非晶态 3.32，其余结构不变。结构示意，按 Notebook 参数绘制。 |
| `figures/10-pcm-phase.png` | 图 2：晶态切到非晶态时，有效折射率降低，固定周期下 Bragg 波长蓝移。曲线为机制示意，不是 EME 谱线。 |
| `figures/23-pcm-spectra.png` | 图 3：左：150 周期时两相的透射谱，阻带位置随相态移动；右：消光比随周期数增长。本次求解，EME，1450–1550 nm。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`14d7e35e04eb0fe5bec8e5a9df9fd6bd8ebbfce365f901e5ee8d146fb5e6a6ab`。

排版更正（2026-11-11）：将 1 个独立公式段标记为 `p.eq`，供统一排版与公式阅读计时；数学内容、数值和上下标不变，待审状态不变。
