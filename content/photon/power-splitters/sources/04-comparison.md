# 待审证据记录：三种分光器，到底怎么选

状态：技术、逐图来源和授权待人审。作者 GitHub 账号尚未提供，`authors` 留空，不得据此安排作者自审。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/example-library
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/YJunction
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/DirectionalCoupler
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/MMIPowerSplitter2x2

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

MMI 端口占比以两路之和归一化，总透射以输入源归一化；三类器件的材料、端口与采样条件不同，不构成同条件排名。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/07-comparison.png` | 图 1：三种分光结构的横向对照。这是机制层面的定性倾向，不是同条件的定量排名。 |
| `figures/08-spectra.png` | 图 2：三个案例的 FDTD 波长响应。上排为上支路基模功率占两路基模输出之和的比例，下排为基模总透射；浅蓝带为本文选定的 1.53–1.57 μm 窗口。定向耦合器的上支路为交叉端，Y 分支下支路由镜像对称推得。 |
| `figures/09-variants.png` | 图 3：四种进阶做法的示意：级联、非等分比、宽带耦合、逆向设计。 |
| `figures/10-workflow.png` | 图 4：从需求到验收的四步。不达标就回到第三步，改参数再扫一次。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`325e6b85f201e0e9c545b424dcf5e51f1b32aab3754db2b99e995b0b6559119a`。
