# 待审证据记录：同样 50 μm，为什么二次轮廓更划算？

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/EdgeCoupler
- https://www.lingcompute.com/photon/learning-center/example-library
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/BilayerSiNEdgeCoupler
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/WaveguideSizeConverter
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/FreeFormCoupler

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

双层 SiN 是层间模式转移，不是上下衍射相消。不同接口不能跨波段直接排名；净通量不等于 TE0。厚度—有效折射率标定的并行实现不改变物理设置。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/08-edge-geometry.svg` | 图 1：三种轮廓的俯视对比（横向宽度放大约 4 倍，纵向按真实比例）。三者起点与终点相同，中途的宽度增速不同，同一段长度里「慢」的位置也不一样。 |
| `figures/09-edge-field.png` | 图 2：倒锥的俯视模场。高斯源的 1/e² 强度直径为 2.5 μm，束腰半径为 1.25 μm；输出波导几何宽度为 0.5 μm。 |
| `video/edge-quadratic-50-GUI-3D-crop.gif` | 动画 1：本次 FDTD 二次倒锥的 GUI 原生场动画，field_xy 监视器，XY 平面 z = 0 μm，1550 nm，Re(Ey)。3D Carpet 的起伏表示场值，展示单频场的相位变化，不是真实脉冲传播录像。 |
| `figures/23-edge-width.svg` | 图 3：截面 ／Ey／² 的二阶矩等效直径沿传播方向变化；对高斯强度分布按 D=4σ 换算。它不是波导几何宽度。 |
| `figures/10-edge-sections.png` | 图 4：尖端与输出端的截面模场。左图还是接近圆形的自由空间模场，右图已经被波导约束成椭圆形。 |
| `figures/11-edge-spectrum.svg` | 图 5：耦合谱。1500–1600 nm 扫描窗口内都在 −0.71 dB 以内，峰略偏向长波侧。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`1b4edf20b53a1c7504e53276759b68bcc0cf1e0ef2ea588e7fe104d1187d48b3`。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/08-edge-geometry.svg` | `b49f2b49b68cda066bf1f4b704939c9485323049f1da22c5e4d20052a6558e6a` | `0304ac3992199d4007ab546b1035af3aabd40a7f3717aa4e07f314fa7a0ec948` |
| `figures/23-edge-width.svg` | `66f0c8329ff34fb6e590e7d9046479422cb1559faccd80b6fd998d6f91f0773c` | `d9becf58f6afa63c67372ffcd7e219d88e4b88006df0b6539312eadd9bcdc3a9` |
| `figures/11-edge-spectrum.svg` | `4a8d39caddeba31430c2c3334f3d023b672fba0c8077ee8738d5fa1e5af5a672` | `fa698e14b71b8726c54885dfc28dc52b733317a25304bdb6149a26dc24611ac2` |

以下原生场图、采样结构图或 GUI 动画保留栅格格式；不把 PNG/GIF 嵌入 SVG 充当可编辑矢量图：

- `figures/09-edge-field.png`
- `video/edge-quadratic-50-GUI-3D-crop.gif`
- `figures/10-edge-sections.png`

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
