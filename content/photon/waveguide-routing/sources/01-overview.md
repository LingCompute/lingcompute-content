# 待审证据记录：光怎么在芯片上拐弯、交叉，还不走错路？

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/EulerWaveguideBend
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/WaveguideCrossing
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/SWGWaveguideCrossing
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/ZeroCrossTalkTE

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

圆弧/Euler 与有包层/裸波导仅在配对条件下作定量比较。交叉串扰为 +y 单侧，需写清净通量还是已存导模。100 弯预算是损耗外推，不是多弯 FDTD。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/01-application.png` | 图 1：同一层光子芯片里，转弯、交叉和并行走线解决的是三种不同的连接需求。示意图，未按比例。 |
| `figures/02-metrics.png` | 图 2：损耗、串扰、面积需要一起看。卡片中的功率与半径数字仅用于解释指标，不是本次求解结果。 |
| `figures/04-curvature.png` | 图 3：本例 Euler 弯采用“两段渐变曲线＋中间圆弧”。两者有效半径都是 4 μm，但 Euler 内部的最小半径约为 2.95 μm。 |
| `figures/05-crossing-principle.png` | 图 4：余弦锥形通过中心展宽整形光束；SWG 通过 Si 中的 SiO2 孔阵调节方向响应。两幅是机制示意，未按比例。 |
| `figures/06-crosstalk-principle.png` | 图 5：两根近距离波导可以周期性地交换功率。右图用更小耦合系数说明抑制串扰的方向；曲线是耦合模理论教学示意。图中 3.5% 是示意峰值，不是本次仿真的串扰读数。 |
| `figures/03-routes.png` | 图 6：四种改进做法各有作用位置；圆弧弯是 Euler 弯的基准对照。分组按机制，不是性能排名。 |
| `figures/07-workflow.png` | 图 7：先给几何约束，再分配损耗与串扰预算，最后核查工艺。这样才能把器件指标变成可用的布线规则。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`a32971c18e4e1666f13b158332c82042db90893bfc9c9388885c269c8f6b64ce`。
