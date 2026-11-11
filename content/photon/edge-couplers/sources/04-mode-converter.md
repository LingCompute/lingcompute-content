# 待审证据记录：片内模斑怎么转换：线性锥、Luneburg 与半透镜

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/WaveguideSizeConverter
- https://www.lingcompute.com/photon/learning-center/example-library
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/EdgeCoupler
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/BilayerSiNEdgeCoupler
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/FreeFormCoupler

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

双层 SiN 是层间模式转移，不是上下衍射相消。不同接口不能跨波段直接排名；净通量不等于 TE0。厚度—有效折射率标定的并行实现不改变物理设置。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/05-lens-principle.png` | 图 1：上为绝热锥，宽度变化一路都很慢；下为透镜，用相位把不同位置的光推向宽波导的模式。 |
| `figures/13-wsc-loss.png` | 图 2：三个设计点的总通量传输谱。各自归一到模式源功率；半透镜与前两者的截面和端口不同，不作统一性能排名。 |
| `figures/12-wsc-fields.png` | 图 3：三种结构的 ／Ey／。线性锥与 Luneburg 从宽到窄，半透镜从窄到宽；各图坐标和色标分别显示，不按亮度排名。 |
| `video/linear-50-GUI-3D-crop.gif` | 动画 1：本次 FDTD 线性锥的 GUI 原生场动画，field 监视器，XY 平面 z = 0.055 μm，1550 nm，Re(Ey)。3D Carpet 起伏表示场值；播放展示单频场的相位变化，不是真实脉冲传播录像。 |
| `video/luneburg-GUI-3D-crop.gif` | 动画 2：本次 FDTD Luneburg 转换器的 GUI 原生场动画，field 监视器，XY 平面 z = 0.055 μm，1550 nm，Re(Ey)。可观察该平面内的干涉图样；起伏表示场值，不代表结构形变。 |
| `video/semilens-GUI-3D-crop.gif` | 动画 3：本次 FDTD 半透镜转换器的 GUI 原生场动画，field 监视器，XY 平面 z = 0.13 μm，1550 nm，Re(Ey)。该监视器高度与前两图不同，Carpet 高度不作跨图定量比较；播放为单频相位演示。 |
| `figures/24-wsc-width.png` | 图 4：截面 ／Ey／² 的二阶矩等效直径 D=4σ，仅截取实际转换段，器件起点对齐为 0。收束与扩束方向不同，不能解读成同一任务的快慢对照。 |
| `figures/14-wsc-modepower.png` | 图 5：出口各模式的功率占比。TE0 占绝大部分，但高阶模也分到了可观的份额。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`402d88343c7d7277f43a24777d5fc962d9af4c8fa6a3338129bf67ef1d63416a`。
