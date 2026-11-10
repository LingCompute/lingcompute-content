# 待审证据记录：双层 SiN 端面耦合：薄层接光，厚层布线

状态：技术、逐图来源和授权待人审。作者 GitHub 账号尚未提供，`authors` 留空，不得据此安排作者自审。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/BilayerSiNEdgeCoupler
- https://www.lingcompute.com/photon/learning-center/example-library
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/EdgeCoupler
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/WaveguideSizeConverter
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/FreeFormCoupler

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

双层 SiN 是层间模式转移，不是上下衍射相消。不同接口不能跨波段直接排名；净通量不等于 TE0。厚度—有效折射率标定的并行实现不改变物理设置。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/20-bilayer-structure.png` | 图 1：双层的对接关系。上层负责把模场撑开，下层在 200 μm 处接手送到波导。上层画得更透明，便于看出相对位置。 |
| `figures/04-bilayer-principle.png` | 图 2：薄上层的端面模式经重叠锥形区转移到厚下层。两层均为 SiN，图为非等比例侧视示意。 |
| `figures/21-bilayer-field.png` | 图 3：y = 0 截面的模场。光从左侧光纤进入，在上层 SiN 中逐渐被约束，到 200 μm 之后交给下层。 |
| `figures/25-bilayer-zoom.png` | 图 4：交接处的放大场图。上层在 200 μm 处开始收窄，下层同时接住模场，到 275 μm 完全交给 0.38 μm 波导。 |
| `figures/22-bilayer-spectrum.png` | 图 5：耦合谱。450–640 nm 内都在 −4 dB 以内，但 400 nm 端明显恶化。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`c4f7f1d88cae2780e2820603dfb4d6def5663139badebfc1aac5a780d5e5e16e`。
