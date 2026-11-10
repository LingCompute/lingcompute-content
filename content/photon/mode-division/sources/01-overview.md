# 待审证据记录：同一根波导里的光，怎么按模式分开？

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
| `figures/01-dimensions.png` | 图 1：同一根波导可以并排承载波长、模式、偏振三个维度，三者靠正交性互不干扰。示意图。 |
| `figures/02-mode-profiles.png` | 图 2：同一根 1.63 μm 宽的总线里，TE0–TE3 的横向分布。本地模式求解结果，不是示意。 |
| `figures/03-phase-matching.png` | 图 3：有效折射率随宽度变化。把总线宽度选在交点上，高阶模就与 400 nm 波导里的基模同步。本次宽度扫描结果。 |
| `figures/04-adc-principle.png` | 图 4：相位失配时功率来回摆但转不干净；相位匹配时能整段搬完。解析示意，非本次仿真。 |
| `figures/05-routes.png` | 图 5：三条路线在面积、工艺与设计自由度上各占一个位置，不能只按效率排序。示意图。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`21a6992983f25366fc5eef46127a90d57bf0ff00789131cf8945123b4c97b11b`。
