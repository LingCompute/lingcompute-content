# 待审证据记录：同样转 90°，Euler 弯为什么能少丢一点光？

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
| `figures/04-curvature.png` | 图 1：圆弧的曲率出现阶跃；本例 Euler 弯两端为渐变曲线，中间接一段恒曲率圆弧。渐变的是曲率，而不只是看起来顺滑的外轮廓。 |
| `figures/08-bend-geometry.png` | 图 2：从本次实际仿真读取的器件俯视结构。端口占位相同，但 Euler 中心线会偏离圆弧，不能按相同最小半径理解。 |
| `figures/09-bend-fields.png` | 图 3：1550 nm 的电场幅值 ／E／，两图使用相同线性色标。图像用来确认光走向哪里，微小损耗差异交给模式端口计算。 |
| `video/euler-circular-GUI-3D-crop.gif` | 动画：本次 FDTD 圆弧弯的 GUI 原生 3D Carpet 动图，XY 平面 z = 105 nm，Re(Hz)，λ = 1550 nm。Hz 垂直于布线平面，便于观察完整转向；这是单频场相位演示，不是真实脉冲传播，起伏表示场值而非结构形变。 |
| `video/euler-euler-GUI-3D-crop.gif` | 动画：本次 FDTD Euler 弯的 GUI 原生 3D Carpet 动图，XY 平面 z = 105 nm，Re(Hz)，λ = 1550 nm。图像用于观察路径与相位；微小损耗差异仍以模式端口读数为准，不能按起伏高度判断。 |
| `figures/10-bend-loss.png` | 图 4：1500–1600 nm 的基模损耗谱。本次 Euler 曲线总体更低；中心波长读数不代表所有几何、所有波段都保持同一比例。 |
| `figures/20-loss-budget.png` | 图 5：这是单弯读数的线性预算外推，不是含 100 个弯的 FDTD 求解；尚未计入直段损耗、反射相干叠加或器件之间的耦合。 |
| `figures/07-workflow.png` | 图 6：先定可用空间，再分配单弯损耗上限，最后核查工艺与累计效应。选型从约束出发，比单独追求最低损耗更有用。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`ce7dd7653552540ecbe89920862fbfc763fb0bda7c614927e58d990c08f4a665`。
