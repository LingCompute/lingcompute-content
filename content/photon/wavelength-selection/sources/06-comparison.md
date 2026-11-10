# 待审证据记录：选波该选什么？把 Q、带宽、面积和可调性一起算

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
| `figures/11-tradeoff.png` | 图 1：四条路线在「面积—调谐」平面上的位置。定性示意，不是同条件性能排名。 |
| `figures/12-selection-tree.png` | 图 2：三个问题定结构，剩下的只是带宽与工艺的细调。流程图。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`45cec0bb6d8e89b4a6016524802bb8b0b8f96348f92e40c1a9e5b677cbda681f`。
