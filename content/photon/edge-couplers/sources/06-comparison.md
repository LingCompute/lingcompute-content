# 待审证据记录：端面接口怎么选：先定波段，再定面积，最后才比 dB

状态：技术、逐图来源和授权待人审。作者 GitHub 账号尚未提供，`authors` 留空，不得据此安排作者自审。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/EdgeCoupler
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/BilayerSiNEdgeCoupler
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/WaveguideSizeConverter
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/FreeFormCoupler
- https://www.lingcompute.com/photon/learning-center/example-library

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

双层 SiN 是层间模式转移，不是上下衍射相消。不同接口不能跨波段直接排名；净通量不等于 TE0。厚度—有效折射率标定的并行实现不改变物理设置。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/18-compare.png` | 图 1：四个案例的扫描窗口。倒锥与模斑转换为 1500–1600 nm，双层 SiN 为 400–640 nm，自由曲面为 650–1050 nm。 |
| `figures/13-wsc-loss.png` | 图 3：线性锥、Luneburg 和半透镜的总通量谱。前两者收束、后者扩束，厚度与端口条件不同。 |
| `figures/27-loss-length.png` | 图 4：器件长度与设计点损耗。长度与损耗之间没有单调关系——最长的双层 SiN 损耗最高，最短的模斑转换损耗最低。 |
| `figures/19-choice.png` | 图 2：按界面位置、波段、面积三个问题走，大多数项目能落到一个答案上。 |
| `figures/02-tolerance.png` | 图 5：两个假设高斯模式的横向偏移损失，仅说明模场尺寸影响，不提供接口容差保证。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`bb02ad3be9093542227516285c97281382a89cbd83a8e674fc40aa9a53352860`。
