# 待审证据记录：模分该选什么？三条路线的边界

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

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
| `figures/22-metrics.png` | 图 22：评价一个模分器件，先问这五个数。卡片中的定义是通用口径，不针对某一具体器件。 |
| `figures/23-tradeoff.png` | 图 23：三条路线的定位。纵轴是定性排序，不是实测指标。 |
| `figures/24-selection.png` | 图 24：先问模式数，再问要不要改模场。示意图，编辑建议。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`e1478350adfe225795eea153a243cbe1442992c793f239be9f94a47bb4bd6c2b`。

编辑更正（2026-11-11）：正文不再指向未随稿公开的 `sources/metrics.json`，改为链接本篇公开的来源与口径说明。原始读数与制作工程仍由制作方保留并安排审核核查；本次未新增数据或重新求解，待审状态不变。
