# 待审证据记录：分波器怎么选：五条约束的联立

状态：技术、逐图来源和授权待人审。作者 GitHub 账号尚未提供，`authors` 留空，不得据此安排作者自审。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/example-library
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/Autograd9WDM
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/MultiplexingMMI

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

MMI 的 EME 结果与逆向设计 FDTD 不作同条件排名；AWG/EDG 为机制说明，没有在本项目复现官方实例。目标函数、透射、串扰与带宽分别核查。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/13-metrics.png` | 图 1：分波器的四个核心指标。插损与串扰是性能，3 dB 带宽与 FSR 是容量约束。 |
| `figures/14-selection.png` | 图 2：分波器的选型顺序。通道数与间隔是硬约束，面积与温控是软约束，结构是最后落地的结果。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`c1b58be0bcb3ce657cbe83710da462d455990028f9eeb9f6b24ae83e599162f3`。
