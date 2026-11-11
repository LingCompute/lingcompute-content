# 待审证据记录：模分该选什么？三条路线的边界

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
| `figures/22-metrics.svg` | 图 22：评价一个模分器件，先问这五个数。卡片中的定义是通用口径，不针对某一具体器件。 |
| `figures/23-tradeoff.svg` | 图 23：三条路线的定位。纵轴是定性排序，不是实测指标。 |
| `figures/24-selection.svg` | 图 24：先问模式数，再问要不要改模场。示意图，编辑建议。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`e1478350adfe225795eea153a243cbe1442992c793f239be9f94a47bb4bd6c2b`。

编辑更正（2026-11-11）：正文不再指向未随稿公开的 `sources/metrics.json`，改为链接本篇公开的来源与口径说明。原始读数与制作工程仍由制作方保留并安排审核核查；本次未新增数据或重新求解，待审状态不变。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/22-metrics.svg` | `fc3762eac2dda11d1f15b3e0981dc28553fe6ff366dd0815548db0d0d44417bb` | `263796f20d1c22637ad9d067cd3e565c2dd45057471094f49532cdd11f9c3298` |
| `figures/23-tradeoff.svg` | `6b7fe95f6ae47227ae6d6df90ce53c4e99457c8631278eafe5d7bc40112af91b` | `1ee8ad9e78c1219e4d8d8f0928138733a0912c07ad5fe1a730c7ca96d3a67926` |
| `figures/24-selection.svg` | `bcecb434bef49e9ca7a3b9a28404078cb0d850ca8d94ce8fd8a3576ceb9e3b1e` | `abd8c0499074ff486c91b533f5a91709c950a0ce30c516a9bcffd6b5c1d9bd65` |

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
