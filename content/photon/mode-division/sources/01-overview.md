# 待审证据记录：同一根波导里的光，怎么按模式分开？

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
| `figures/01-dimensions.svg` | 图 1：同一根波导可以并排承载波长、模式、偏振三个维度，三者靠正交性互不干扰。示意图。 |
| `figures/02-mode-profiles.png` | 图 2：同一根 1.63 μm 宽的总线里，TE0–TE3 的横向分布。本地模式求解结果，不是示意。 |
| `figures/03-phase-matching.svg` | 图 3：有效折射率随宽度变化。把总线宽度选在交点上，高阶模就与 400 nm 波导里的基模同步。本次宽度扫描结果。 |
| `figures/04-adc-principle.svg` | 图 4：相位失配时功率来回摆但转不干净；相位匹配时能整段搬完。解析示意，非本次仿真。 |
| `figures/05-routes.svg` | 图 5：三条路线在面积、工艺与设计自由度上各占一个位置，不能只按效率排序。示意图。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`21a6992983f25366fc5eef46127a90d57bf0ff00789131cf8945123b4c97b11b`。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/01-dimensions.svg` | `a3b30eac0b9abc05007818fcb39b420195f4591e02aae46a054fc9695d4c012f` | `373e90d36cf1bdff5e74d63519158d8ea6b2b57b50d71e940a190f257cf4fbec` |
| `figures/03-phase-matching.svg` | `24adfe6feef61e7d7601e4cdcfbba3f1448f63875d12232da33a056bae45a127` | `e75a966bfa22a30c91a44980e09de982f64b0982a3e4608c5fc3accd45eb0cb9` |
| `figures/04-adc-principle.svg` | `ebac347c6d7a47bbd47238e1ff88b39dbd19f80517193e6a72c845b1c8a35d1b` | `8e6766dbc68426796b431648105b75df5cee5a2643fcd2da9ab13b8dc8747378` |
| `figures/05-routes.svg` | `36e535c83a16dae10ef4c03f75b011e023d81ec8cb0ba3faf72e7835445c6ab1` | `3fac3a258ecc4019ba399af2a8e24d27e7395d55c3fe2db413150de09b4cf531` |

以下原生场图、采样结构图或 GUI 动画保留栅格格式；不把 PNG/GIF 嵌入 SVG 充当可编辑矢量图：

- `figures/02-mode-profiles.png`

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
