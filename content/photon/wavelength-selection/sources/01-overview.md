# 待审证据记录：一个波长怎么被挑出来？

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
| `figures/01-application.png` | 图 1：同一根波导里跑着三个波长，选波器件把它们分别送到不同出口。示意图，未按比例。 |
| `figures/02-metrics.png` | 图 2：六个指标各自回答一个问题。卡片中的定义为通用口径，不针对某一具体器件。 |
| `figures/03-two-ways.png` | 图 3：左边靠谐振把光「留」在环里，右边靠周期结构把光「退」回去。两幅均为机制示意。 |
| `figures/04-fsr.png` | 图 4：同一个环的周期性谐振峰，各峰对应不同级次，不是已经分到独立端口的通道。教学示意。 |
| `figures/11-tradeoff.png` | 图 5：几类结构的尺寸与控制复杂度示意，具体位置随平台、通道数和漂移预算变化。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`62954e8f6c5f99aca708dc5b6b8d817e2ae1e371acafe7e7892426810d23ff71`。
