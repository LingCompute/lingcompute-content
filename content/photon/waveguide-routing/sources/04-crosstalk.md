# 待审证据记录：两根波导没有接触，光为什么也会串过去？

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/ZeroCrossTalkTE
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/EulerWaveguideBend
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/WaveguideCrossing
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/SWGWaveguideCrossing

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

圆弧/Euler 与有包层/裸波导仅在配对条件下作定量比较。交叉串扰为 +y 单侧，需写清净通量还是已存导模。100 弯预算是损耗外推，不是多弯 FDTD。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/06-crosstalk-principle.png` | 图 1：左图示意普通近距离波导的能量交换；右图示意耦合系数减小后，同样长度里的交换受到抑制。曲线是教学模型，不是本次仿真数据。 |
| `figures/17-cladding-geometry.png` | 图 2：完整器件与中央局部的实际几何。中间并行段长 100 μm，细栅的最小尺寸与输出弯道都属于需要实现的结构。 |
| `figures/18-cladding-fields.png` | 图 3：裸波导对照中，邻路可见被耦合进去的场；加包层后，邻路在同一线性色标下明显更暗。图像用于看现象，串扰数值由端口读取。 |
| `video/xtalk-ref-GUI-3D-crop.gif` | 动画：本次 FDTD 裸并行波导的 GUI 原生 3D Carpet 动图，XY 平面 z = 0，Re(Ey)，λ = 1550 nm。展示单频场相位变化，起伏表示场值，不是真实脉冲传播；邻路功率仍由输出端口统计。 |
| `video/xtalk-eskid-GUI-3D-crop.gif` | 动画：本次 FDTD 各向异性包层波导的 GUI 原生 3D Carpet 动图，XY 平面 z = 0，Re(Ey)，λ = 1550 nm。起伏高度不能用来跨图比较场强；邻路较暗也不等于严格零串扰。 |
| `figures/19-cladding-spectra.png` | 图 4：1500–1600 nm 的串扰谱。SWG 包层在约 1547 nm 有深谷；到波段两端，串扰会升高，所以单点数字不能代替带宽指标。 |
| `figures/02-metrics.png` | 图 5：损耗、串扰与面积互相牵制。图中数字是教学示例；实际选择还要加上最小尺寸、带宽和加工偏差的约束。 |
| `figures/21-tradeoffs.png` | 图 6：从布线瓶颈选择结构。只有长距离靠近走线的问题，才需要优先评估这类包层；它与十字交叉解决的是不同场景。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`0f18028245c25c4765ff2df598340bace05f4ac8651df5a8ee3e0369b765d048`。
