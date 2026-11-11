# 待审证据记录：光怎么在芯片上拐弯、交叉，还不走错路？

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
| `figures/01-application.svg` | 图 1：同一层光子芯片里，转弯、交叉和并行走线解决的是三种不同的连接需求。示意图，未按比例。 |
| `figures/02-metrics.svg` | 图 2：损耗、串扰、面积需要一起看。卡片中的功率与半径数字仅用于解释指标，不是本次求解结果。 |
| `figures/04-curvature.svg` | 图 3：本例 Euler 弯采用“两段渐变曲线＋中间圆弧”。两者有效半径都是 4 μm，但 Euler 内部的最小半径约为 2.95 μm。 |
| `figures/05-crossing-principle.svg` | 图 4：余弦锥形通过中心展宽整形光束；SWG 通过 Si 中的 SiO2 孔阵调节方向响应。两幅是机制示意，未按比例。 |
| `figures/06-crosstalk-principle.svg` | 图 5：两根近距离波导可以周期性地交换功率。右图用更小耦合系数说明抑制串扰的方向；曲线是耦合模理论教学示意。图中 3.5% 是示意峰值，不是本次仿真的串扰读数。 |
| `figures/03-routes.svg` | 图 6：四种改进做法各有作用位置；圆弧弯是 Euler 弯的基准对照。分组按机制，不是性能排名。 |
| `figures/07-workflow.svg` | 图 7：先给几何约束，再分配损耗与串扰预算，最后核查工艺。这样才能把器件指标变成可用的布线规则。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`a32971c18e4e1666f13b158332c82042db90893bfc9c9388885c269c8f6b64ce`。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/01-application.svg` | `ac83d02f59776302691fec0e189e53b29998ace95c3ac7928abefada302acfdd` | `93ce8aa482859c05ff1736d73ffa35d7b278b2d19c89cf1727178d2640913a13` |
| `figures/02-metrics.svg` | `3c6c1cf39ece7e89b2a6893a29127296a20769764050a8e865032ec4d21646dc` | `33152d59dae02851794828ddc3df7327c0bc44053e8d18dac90ffcbffc1b8d58` |
| `figures/04-curvature.svg` | `b8390d7442e70f2ed9137e388c3a503db04deca68d7e7ac9b100b1523940baa4` | `ecf9afdde79880751969f2a6f07e12983596842c028e5ab1a7ab80b3db1762b5` |
| `figures/05-crossing-principle.svg` | `57d1b01e355449e55c4be27d0a1c4cf8e7ee86ff92f7364404ab07c85766e3c8` | `bd29703829f35f321bc912918eb6e76acf214810463c4a9ba870718bb1360b84` |
| `figures/06-crosstalk-principle.svg` | `c82c530fca79392fbcf4e9ca5c2fd77ce051ea1aeef9947d26dc7125e80f2cd9` | `8332e09f3936fe127696ab99545459339427cc47631a19ead74cc157b5fa2b86` |
| `figures/03-routes.svg` | `249779a8ec738d3dc515e002e47e1f97576624b5eafc3049d105bf63dc0f9ffa` | `827da6078d60f4d8a04d2eab274908a1f1440e6a5dac2884876c83f4a208e512` |
| `figures/07-workflow.svg` | `70e8a879998dd46503a1d9c3a3cd0f2dc841b63fafb7294ab3a89de1d79368cf` | `dedb2d073861ed1c65252f3d432109f28e0494789289059008a64c85f1756100` |

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
