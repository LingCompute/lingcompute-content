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
| `figures/05-lens-principle.svg` | 图 1：上为绝热锥，宽度变化一路都很慢；下为透镜，用相位把不同位置的光推向宽波导的模式。 |
| `figures/13-wsc-loss.svg` | 图 2：三个设计点的总通量传输谱。各自归一到模式源功率；半透镜与前两者的截面和端口不同，不作统一性能排名。 |
| `figures/12-wsc-fields.png` | 图 3：三种结构的 ／Ey／。线性锥与 Luneburg 从宽到窄，半透镜从窄到宽；各图坐标和色标分别显示，不按亮度排名。 |
| `video/linear-50-GUI-3D-crop.gif` | 动画 1：本次 FDTD 线性锥的 GUI 原生场动画，field 监视器，XY 平面 z = 0.055 μm，1550 nm，Re(Ey)。3D Carpet 起伏表示场值；播放展示单频场的相位变化，不是真实脉冲传播录像。 |
| `video/luneburg-GUI-3D-crop.gif` | 动画 2：本次 FDTD Luneburg 转换器的 GUI 原生场动画，field 监视器，XY 平面 z = 0.055 μm，1550 nm，Re(Ey)。可观察该平面内的干涉图样；起伏表示场值，不代表结构形变。 |
| `video/semilens-GUI-3D-crop.gif` | 动画 3：本次 FDTD 半透镜转换器的 GUI 原生场动画，field 监视器，XY 平面 z = 0.13 μm，1550 nm，Re(Ey)。该监视器高度与前两图不同，Carpet 高度不作跨图定量比较；播放为单频相位演示。 |
| `figures/24-wsc-width.svg` | 图 4：截面 ／Ey／² 的二阶矩等效直径 D=4σ，仅截取实际转换段，器件起点对齐为 0。收束与扩束方向不同，不能解读成同一任务的快慢对照。 |
| `figures/14-wsc-modepower.svg` | 图 5：出口各模式的功率占比。TE0 占绝大部分，但高阶模也分到了可观的份额。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`402d88343c7d7277f43a24777d5fc962d9af4c8fa6a3338129bf67ef1d63416a`。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/05-lens-principle.svg` | `e9a1a85e4ec91648c7e9b6a002c5c19679d151486741b3847c86fa57d071deab` | `1664ec80f87d3d2a76418097fd0567f38644ee815db588c8dcac8793d3da14eb` |
| `figures/13-wsc-loss.svg` | `f7f25a80ebd2e2a39f310785c42a21b2b37875fcf4737e70475cfb42002814df` | `7a683fbbfecd0da042398818afb300773c31c6b7efb8fcbf135fbd87782968f9` |
| `figures/24-wsc-width.svg` | `7e2a4fa1377faaa950e7566ef3d5f9928f49e922b76001075a2d08a63f898ada` | `e27074230c55907e8a9cb6f15221c00d9cffcc9ebe5c6519c601f2ca3af0b5da` |
| `figures/14-wsc-modepower.svg` | `49cedf092d97a72bf5e6deb790c12c283b4497fcd32b6fca43b80d433046efb0` | `b0399f10cf98756465e073d6511a2a49b66cdad749a730df9ea2b9b44e268890` |

以下原生场图、采样结构图或 GUI 动画保留栅格格式；不把 PNG/GIF 嵌入 SVG 充当可编辑矢量图：

- `figures/12-wsc-fields.png`
- `video/linear-50-GUI-3D-crop.gif`
- `video/luneburg-GUI-3D-crop.gif`
- `video/semilens-GUI-3D-crop.gif`

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
