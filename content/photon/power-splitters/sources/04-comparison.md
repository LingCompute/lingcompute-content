# 待审证据记录：三种分光器，到底怎么选

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/example-library
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/YJunction
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/DirectionalCoupler
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/MMIPowerSplitter2x2

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

MMI 端口占比以两路之和归一化，总透射以输入源归一化；三类器件的材料、端口与采样条件不同，不构成同条件排名。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/07-comparison.svg` | 图 1：三种分光结构的横向对照。这是机制层面的定性倾向，不是同条件的定量排名。 |
| `figures/08-spectra.svg` | 图 2：三个案例的 FDTD 波长响应。上排为上支路基模功率占两路基模输出之和的比例，下排为基模总透射；浅蓝带为本文选定的 1.53–1.57 μm 窗口。定向耦合器的上支路为交叉端，Y 分支下支路由镜像对称推得。 |
| `figures/09-variants.svg` | 图 3：四种进阶做法的示意：级联、非等分比、宽带耦合、逆向设计。 |
| `figures/10-workflow.svg` | 图 4：从需求到验收的四步。不达标就回到第三步，改参数再扫一次。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`325e6b85f201e0e9c545b424dcf5e51f1b32aab3754db2b99e995b0b6559119a`。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/07-comparison.svg` | `24d76f0d6efe0c8b50138a30533562da2aab750a9be3894a98911aa2282c739e` | `a6866426a42e42cfa97e66dabfebeabb9dc38ad119c01e7de9cbb0058b0e164b` |
| `figures/08-spectra.svg` | `963e7e3c6b880d6a577fcd3d6bd3778ab3fece3f2f067baecee11a9873e08148` | `75424b894b1808f91e81a51db3e9d371fe3fac98875bb89370498f430aa5b3c5` |
| `figures/09-variants.svg` | `39c5038fa7b02b6dbee6b44a0ccdb62337b37d527bfa758420b1bacf07928e5d` | `5b392af6ab5fbfbe57c117e2bd15620fe9b226ba35ef675e5577a54632a68b4a` |
| `figures/10-workflow.svg` | `c923490da4eee6122d51b68ce3f8d456aef2b01ce53a56ecd56a4c89c7689830` | `cc7e5899f7972891cc8f2945827aca6458076b55366d9ca544445528e9850393` |

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
