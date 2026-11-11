# 待审证据记录：不画结构，只写目标：逆向设计怎么长出一个模式转换器

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
| `figures/13-invdes-flow.svg` | 图 13：逆向设计的五个环节，前向与伴随各跑一次得到梯度，再更新参数。示意图。 |
| `figures/14-invdes-structure.png` | 图 14：左边是随机初值，右边是二十步之后的结构。设计区 5×3 μm，一格 100 nm。本次优化结果。 |
| `figures/15-invdes-modes.svg` | 图 15：输入端的目标是基模（mode 0），输出端要的是它的上一阶（mode 2）。两个形状不同，这就是要「搬」的东西。本地模式求解。 |
| `figures/16-invdes-convergence.svg` | 图 16：目标函数随迭代步上升，末点是参数更新后的复核值。本次优化结果。 |
| `figures/17-invdes-field.png` | 图 17：1.0 μm 波长下的 ／E／²（dB，相对峰值）。左侧基模进入，中间 5×3 μm 的设计区把场重塑，输出端分成两支。本次求解结果。 |
| `video/invdes-final-GUI-2D-crop.gif` | 动画 1：本次 FDTD 最终结构复核的 GUI 原生二维动图，field_mnt 监视器，XY 平面 z = 0 μm，1000 nm，Re(Ez)。左侧基模进入，右侧输出呈双瓣分布。这是原有二维模型的单频相位循环，不是真实脉冲传播录像，也不是结构优化的迭代过程。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`e6f638f1e029f2900b1920e985d7c802769941d975dc7fa225bd5ce3355cc756`。

编辑与排版更正（2026-11-11）：将 `series.json` 摘要中的“实测功率”改为“仿真功率”，与正文的二维 FDTD 说明一致；将 1 个独立公式段标记为 `p.eq`，供统一排版与公式阅读计时。数学内容、数值和上下标不变，待审状态不变，本次未重新求解。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/13-invdes-flow.svg` | `25cfd269a8cff5d08b8236a6aa859bbb0e8cd25e82918fcccb9738f5db8a5da5` | `bf2271c3ffe7418ed9478cb17f4ca3c9eca4d691e692598dec20a540e222070a` |
| `figures/15-invdes-modes.svg` | `1218f640fcfca3e171fd875046498f9473fa4b9a41da1e9923b4c2bdc5330e92` | `5065c32f74b2e64b896204ad23ca693dba659b9b47993b65e9107b1d5ce4a30d` |
| `figures/16-invdes-convergence.svg` | `33c29a04264eff90eafab4791d4a286f329a7e1767b7b1fc3ccca646ec1d123b` | `f3285e9650afb4e8089c43c5ac47e9685018b2e32bca81fb1e87a4d32a48fe7e` |

以下原生场图、采样结构图或 GUI 动画保留栅格格式；不把 PNG/GIF 嵌入 SVG 充当可编辑矢量图：

- `figures/14-invdes-structure.png`
- `figures/17-invdes-field.png`
- `video/invdes-final-GUI-2D-crop.gif`

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
