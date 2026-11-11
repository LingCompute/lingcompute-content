# 待审证据记录：布线该选什么？把损耗、串扰和工艺一起算

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/EulerWaveguideBend
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/WaveguideCrossing
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/SWGWaveguideCrossing
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/ZeroCrossTalkTE

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

圆弧/Euler 与有包层/裸波导仅在配对条件下作定量比较。交叉串扰为 +y 单侧，需写清净通量还是已存导模。100 弯预算是损耗外推，不是多弯 FDTD。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/03-routes.svg` | 图 1：四种改进做法与一个圆弧基准。先找到几何位置和物理机制，再决定该比较哪一组模型。 |
| `figures/10-bend-loss.svg` | 图 2：本次两种弯的基模损耗谱。比较约束是相同有效半径；Euler 的内部最小半径更小，不能换成“相同最小半径”的结论。 |
| `figures/13-cosine-spectra.svg` | 图 3：余弦锥形交叉采用净通量取数；串扰是 +y 侧口 / 直行口。另一个侧口、反射与输出模式需要按设计目标补充统计。 |
| `figures/16-swg-spectra.svg` | 图 4：SWG 在 1950 nm 的 TE0 插损约 0.461 dB，TE0 单侧串扰约 −42.66 dB；统计所存三个模式后，单侧串扰约 −39.92 dB。 |
| `figures/19-cladding-spectra.svg` | 图 5：包层显著压低了本例串扰，但深谷随波长变化明显。最低点不是整个工作带宽的代表，也未经过网格和加工容差收敛证明。 |
| `figures/21-tradeoffs.svg` | 图 6：优先采用能解决当前瓶颈的结构。增加设计自由度时，也要加入相应的加工与验证工作。 |
| `figures/07-workflow.svg` | 图 7：几何 → 损耗预算 → 串扰上限 → 工艺核查。对候选结构完成同条件验证后，再把它放进完整链路。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`6a03bbde910109bd0fbe60b18308a7744a5de4946bcffbe5b108877014f00ead`。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/03-routes.svg` | `249779a8ec738d3dc515e002e47e1f97576624b5eafc3049d105bf63dc0f9ffa` | `827da6078d60f4d8a04d2eab274908a1f1440e6a5dac2884876c83f4a208e512` |
| `figures/10-bend-loss.svg` | `9fd24fb394ed424900b81b3804527d7c94a5d63ce1305c79c00db0ccb8f40579` | `8229cde30b36e4f621469d2673be1e5ac21050d860503695d933909c439ef05b` |
| `figures/13-cosine-spectra.svg` | `9aaa3fdcf06f37909dcda8ece380847ac60b95822277e8f748b4721d479bae27` | `364161731e007a5187b13a378d60396eddf43c551e36aac0a6648cd92e705f97` |
| `figures/16-swg-spectra.svg` | `b39a31653dc809e95ed51d8dc7f75458bc952ffcc2fb632a897a840771ea2aab` | `49f108183285bdea3cb4075b6a2389a061645375a61faebb8f7dfd2bc9c720a1` |
| `figures/19-cladding-spectra.svg` | `14d5e590b77e50d2ef8c21bc1a24125245c861082f0c148b6f985af4f91e7b50` | `f44157b02cf9d9f262aaf4ad1d85be14ee2d164100d1c3f77095c8b40e76765c` |
| `figures/21-tradeoffs.svg` | `93d2c4e2b82cc74fa41288396645869eb11ba43305caaa1446d1b0e8cc35f8fd` | `a277c5e7b9c52e0bf460d1cfb8fcdbd498c1b346d90b151b4c92922cf148f329` |
| `figures/07-workflow.svg` | `70e8a879998dd46503a1d9c3a3cd0f2dc841b63fafb7294ab3a89de1d79368cf` | `dedb2d073861ed1c65252f3d432109f28e0494789289059008a64c85f1756100` |

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
