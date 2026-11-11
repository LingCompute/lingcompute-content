# 待审证据记录：布线该选什么？把损耗、串扰和工艺一起算

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
| `figures/03-routes.png` | 图 1：四种改进做法与一个圆弧基准。先找到几何位置和物理机制，再决定该比较哪一组模型。 |
| `figures/10-bend-loss.png` | 图 2：本次两种弯的基模损耗谱。比较约束是相同有效半径；Euler 的内部最小半径更小，不能换成“相同最小半径”的结论。 |
| `figures/13-cosine-spectra.png` | 图 3：余弦锥形交叉采用净通量取数；串扰是 +y 侧口 / 直行口。另一个侧口、反射与输出模式需要按设计目标补充统计。 |
| `figures/16-swg-spectra.png` | 图 4：SWG 在 1950 nm 的 TE0 插损约 0.461 dB，TE0 单侧串扰约 −42.66 dB；统计所存三个模式后，单侧串扰约 −39.92 dB。 |
| `figures/19-cladding-spectra.png` | 图 5：包层显著压低了本例串扰，但深谷随波长变化明显。最低点不是整个工作带宽的代表，也未经过网格和加工容差收敛证明。 |
| `figures/21-tradeoffs.png` | 图 6：优先采用能解决当前瓶颈的结构。增加设计自由度时，也要加入相应的加工与验证工作。 |
| `figures/07-workflow.png` | 图 7：几何 → 损耗预算 → 串扰上限 → 工艺核查。对候选结构完成同条件验证后，再把它放进完整链路。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`6a03bbde910109bd0fbe60b18308a7744a5de4946bcffbe5b108877014f00ead`。
