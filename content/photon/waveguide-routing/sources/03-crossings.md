# 待审证据记录：两条波导十字相交，怎样让光各走各的？

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/WaveguideCrossing
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/SWGWaveguideCrossing
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/EulerWaveguideBend
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/ZeroCrossTalkTE

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

圆弧/Euler 与有包层/裸波导仅在配对条件下作定量比较。交叉串扰为 +y 单侧，需写清净通量还是已存导模。100 弯预算是损耗外推，不是多弯 FDTD。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/05-crossing-principle.svg` | 图 1：左侧通过中心展宽调节束形，右侧通过孔阵占空比改变方向响应。机制示意未按比例，不能从图中直接比较面积。 |
| `figures/11-cosine-geometry.svg` | 图 2：本次求解的实际结构。光由左侧进入；右侧是直行口，上方 +y 是记录串扰的侧口。模型没有把上下两侧的串扰通量加在一起。 |
| `figures/12-cosine-field.png` | 图 3：1310 nm 的电场幅值 ／E／。光在展宽区发生整形，主要沿水平方向进入对面端口；侧臂中较弱的场仍需要端口统计确认。 |
| `video/crossing-cosine-GUI-3D-crop.gif` | 动画：本次 FDTD 余弦锥形交叉的 GUI 原生 3D Carpet 动图，XY 平面 z = 0，Re(Ey)，λ = 1310 nm。展示单频场相位变化，起伏表示场值，不是结构形变或真实脉冲传播；串扰仍以端口统计为准。 |
| `figures/13-cosine-spectra.svg` | 图 4：1260–1360 nm 内的插损与单侧串扰。插损按 −10 log10(T) 记为正值；原 Notebook 的负值透射 dB 曲线在本文中做了符号统一。 |
| `figures/14-swg-geometry.svg` | 图 5：从实际模型重绘的孔阵及局部放大。方向差异来自矩形孔与占空比布局；蓝色为硅，浅色孔区为二氧化硅。 |
| `figures/15-swg-field.png` | 图 6：本次 TE0 入射的场图，波长为 1917.95 nm。这个值来自源的中心频率；后面用 1950 nm 作为谱线示例读数，两者并不相同。 |
| `video/swg-TE0-GUI-3D-crop.gif` | 动画：本次 FDTD SWG 交叉的 GUI 原生 3D Carpet 动图，TE0 入射，XY 平面 z = 0，Re(Ey)，λ ≈ 1917.95 nm。展示单频场相位变化，起伏表示场值，不是真实脉冲传播；不能据此推断 TE1 或 TE2 入射性能。 |
| `figures/16-swg-spectra.svg` | 图 7：1700–2200 nm 的 TE0 插损，以及两种模式统计口径下的单侧串扰。三个已记录模式之和仍不等于所有辐射、全部模式和全部端口的泄漏。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`1b598a78b7e26e4a7d1ee537bc43a403a7810483655d7503f2bdbec7b145308a`。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/05-crossing-principle.svg` | `57d1b01e355449e55c4be27d0a1c4cf8e7ee86ff92f7364404ab07c85766e3c8` | `bd29703829f35f321bc912918eb6e76acf214810463c4a9ba870718bb1360b84` |
| `figures/11-cosine-geometry.svg` | `b17c4c34df3ea8f5293e2123f3f9083a041a2c606d29359246a7bd611907623f` | `96836633b1b62a66870ec47b97006c465c08ddbefda5c3e5fdb0cee2154319fb` |
| `figures/13-cosine-spectra.svg` | `9aaa3fdcf06f37909dcda8ece380847ac60b95822277e8f748b4721d479bae27` | `364161731e007a5187b13a378d60396eddf43c551e36aac0a6648cd92e705f97` |
| `figures/14-swg-geometry.svg` | `d1bde8a670ce8e3a9ed98fe3770bcc89b4b5f98a6afa5e59252b15d8cb625b1b` | `05d000edd182a0ac65f6628cd4c2474beffdef72e46132a8c1ebd976f2d4c4b2` |
| `figures/16-swg-spectra.svg` | `b39a31653dc809e95ed51d8dc7f75458bc952ffcc2fb632a897a840771ea2aab` | `49f108183285bdea3cb4075b6a2389a061645375a61faebb8f7dfd2bc9c720a1` |

以下原生场图、采样结构图或 GUI 动画保留栅格格式；不把 PNG/GIF 嵌入 SVG 充当可编辑矢量图：

- `figures/12-cosine-field.png`
- `video/crossing-cosine-GUI-3D-crop.gif`
- `figures/15-swg-field.png`
- `video/swg-TE0-GUI-3D-crop.gif`

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
