# 待审证据记录：同一块材料，怎么让阻带搬家？

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
| `figures/09-pcm-structure.svg` | 图 1：Si 波导上周期排布 Sb2Se3 块。晶态折射率 4.16，非晶态 3.32，其余结构不变。结构示意，按 Notebook 参数绘制。 |
| `figures/10-pcm-phase.svg` | 图 2：晶态切到非晶态时，有效折射率降低，固定周期下 Bragg 波长蓝移。曲线为机制示意，不是 EME 谱线。 |
| `figures/23-pcm-spectra.svg` | 图 3：左：150 周期时两相的透射谱，阻带位置随相态移动；右：消光比随周期数增长。本次求解，EME，1450–1550 nm。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`14d7e35e04eb0fe5bec8e5a9df9fd6bd8ebbfce365f901e5ee8d146fb5e6a6ab`。

排版更正（2026-11-11）：将 1 个独立公式段标记为 `p.eq`，供统一排版与公式阅读计时；数学内容、数值和上下标不变，待审状态不变。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/09-pcm-structure.svg` | `fc95f17380125fc16f0f957dcfb61a470113dfd69cd6758a38d85115b10710d5` | `de1233024e90f4cecf8d632a0d7c773112af8926675afc8fc6e236a0cf476b3d` |
| `figures/10-pcm-phase.svg` | `84fafe97f2bc19517dac12a947df36e8d08cebcf945c5a7d5dc0fbd895aa12e5` | `e5ea7f6d0e17890bc06c40f7d2c74dd6b9410dcd9636b1e8092f03e2d5739c38` |
| `figures/23-pcm-spectra.svg` | `3f185d23648ae0e4da52f734a6187c46283f5fce81a47c380fde004c257790d0` | `654ab6f9876c44548a4fc279c0e6b721b2c0837b9bc6ef5fb9fc4b5e9ee7ddb9` |

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
