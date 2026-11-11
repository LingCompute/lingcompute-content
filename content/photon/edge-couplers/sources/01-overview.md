# 待审证据记录：光怎么从芯片边缘进出？先把两种接口分清

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/EdgeCoupler
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/BilayerSiNEdgeCoupler
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/WaveguideSizeConverter
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/FreeFormCoupler
- https://www.lingcompute.com/photon/learning-center/example-library

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

双层 SiN 是层间模式转移，不是上下衍射相消。不同接口不能跨波段直接排名；净通量不等于 TE0。厚度—有效折射率标定的并行实现不改变物理设置。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/01-interfaces.svg` | 图 1：两种接口的方向。左为面外（光栅），光被折出表面；右为面内（端面），光沿芯片平面直接进出。 |
| `figures/02-tolerance.svg` | 图 2：两个假设高斯模场的偏移重叠。w 为束腰半径；曲线仅说明模场尺寸的影响，不代表两类接口的实测容差。 |
| `figures/03-four-routes.svg` | 图 3：四种接口或模场转换案例。倒锥靠缓变轮廓；双层 SiN 用薄层接光、厚层布线；透镜型转换调整波前；自由曲面用反射面改变光路。 |
| `figures/11-edge-spectrum.svg` | 图 4：倒锥的高斯光束到输出基模耦合谱。后续案例会分别说明自己的功率口径。 |
| `figures/12-wsc-fields.png` | 图 5：三种模斑转换方案的场分布。长度差三倍以上，机制也完全不同。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`d598254c42b9ff2b68a9ca0bf1fd4054e09314c0e46cc0c73761be386b775361`。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/01-interfaces.svg` | `dc3bc1a9c239e92f6970afb129c57bb16aabffc04c427a25f2bf5aac289126c7` | `005e339cf3ef385d3f51985e8caba31d5dccfbc5e3e9d5f4d44138d9f0e4fd91` |
| `figures/02-tolerance.svg` | `61ce121aed841fc1301ef70e68ee11357590f0a8c7f1506d050f09efa32bf4a7` | `ee0e394c40d9fbdbe17120bad084e25706bc24e4a675a0675e80d2e06efa8e35` |
| `figures/03-four-routes.svg` | `96196662978f47d2f44b68ec31a194550d314f7d121667c48eca3400fa27dc29` | `f0a9cfa540110cfa38e9d3810d04f532f92e1c458bd56a2f1b18d61d5a1adfd7` |
| `figures/11-edge-spectrum.svg` | `4a8d39caddeba31430c2c3334f3d023b672fba0c8077ee8738d5fa1e5af5a672` | `fa698e14b71b8726c54885dfc28dc52b733317a25304bdb6149a26dc24611ac2` |

以下原生场图、采样结构图或 GUI 动画保留栅格格式；不把 PNG/GIF 嵌入 SVG 充当可编辑矢量图：

- `figures/12-wsc-fields.png`

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
