# 待审证据记录：不写几何，只写目标

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/Autograd9WDM
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/MultiplexingMMI

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

MMI 的 EME 结果与逆向设计 FDTD 不作同条件排名；AWG/EDG 为机制说明，没有在本项目复现官方实例。目标函数、透射、串扰与带宽分别核查。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/11-design-region.svg` | 图 1：设计区与端口。4.5×4.5 μm 的方块被切成 300×300 个像素，每个像素的填充率都是优化变量。示意，颜色不代表真实优化结果。 |
| `figures/12-objective.svg` | 图 2：目标函数的四层结构。前两层管光学性能，第三层管可制造性，第四层管通道均衡。 |
| `figures/17-wdm-convergence.svg` | 图 3：目标函数随迭代的变化。前 1/3 只提透射，之后加入串扰惩罚，曲线出现一次台阶。本次运行，2D，50 步。 |
| `figures/18-wdm-spectra.svg` | 图 4：四个出口的透射谱。每个口在自己对应的波长上出现峰值，其余波长被压低。本次运行，151 点采样。 |
| `figures/19-wdm-matrix.svg` | 图 5：通道功率矩阵。行是出口，列是通道，数值为通道带宽内 5 点平均功率。本次运行。 |
| `video/wdm-final-1270-GUI-XY-crop.gif` | 动画 1：本次 FDTD 末态的 1270 nm XY 场，GUI 原生导出，Re(Ez)。对应 mode_0 出口，y = −1.6875 μm。 |
| `video/wdm-final-1290-GUI-XY-crop.gif` | 动画 2：本次 FDTD 末态的 1290 nm XY 场，GUI 原生导出，Re(Ez)。对应 mode_1 出口，y = −0.5625 μm。 |
| `video/wdm-final-1310-GUI-XY-crop.gif` | 动画 3：本次 FDTD 末态的 1310 nm XY 场，GUI 原生导出，Re(Ez)。对应 mode_2 出口，y = +0.5625 μm。 |
| `video/wdm-final-1330-GUI-XY-crop.gif` | 动画 4：本次 FDTD 末态的 1330 nm XY 场，GUI 原生导出，Re(Ez)。对应 mode_3 出口，y = +1.6875 μm。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`dfccec935f6655cdb4367ad6ef5dbd2af5a155b1192560df53db17268e1c0971`。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/11-design-region.svg` | `479b5b13fd91c27eb2997e68f23249cec90b6acac78720ef8848f82bb7ef4bfe` | `4b7eac4cc2d53d4c10eb8bc4546221f9325c66bdb9f61ea0a385fb0ff94f2f46` |
| `figures/12-objective.svg` | `1c528604380e6db0973d31d10c4f04927899f941d942afa761fbe87b27970c69` | `2e95681a86e4871c436086c6d67ad96c4dca539bec027f9e4fc302931d4def46` |
| `figures/17-wdm-convergence.svg` | `12a5a0773e763df135ab295263abf6e6d7d0b5d18155bed21e5bb73731bd8538` | `f5f510b84c575ec3a8b2c25a5aefcc292569f3b928f850a08396aa6cc460738a` |
| `figures/18-wdm-spectra.svg` | `8f7a21b1da7e038fac7c3d49d777c23a20257d08824ca0f2a3824cfd6e49a426` | `72a331f9a23c8eb8fe8d17bfde2efb1c4bc8f23d19344452dec4c01e8378ad6d` |
| `figures/19-wdm-matrix.svg` | `ee58b6a49a7671a6861fb8d2a7b9c485e0fbc8c761249dc97079ae75e99c27ab` | `67b522e7e972cf2c53229664c56740515402931f50b62817a300759faaa41d3d` |

下列数据图复用原工程绘图函数与保存的数据重新导出，色块及色标均为矢量对象，未重新运行求解：

- `figures/19-wdm-matrix.svg`：数据 `wdm-spectra.npz`，SHA256 `f9f5e0f5fe0477607063a2dfdea3eefa5a2dda0e91ff20eaaaba866ea0c6b75d`；沿用 `wdm_matrix` 的坐标、数值及色标。

通道功率矩阵的格内读数（与图中相同，行是输出口，列为 1270／1290／1310／1330 nm）：

| 输出口 | 1270 nm | 1290 nm | 1310 nm | 1330 nm |
| --- | --- | --- | --- | --- |
| 出口 1 | 0.930 | 0.015 | 0.002 | 0.001 |
| 出口 2 | 0.009 | 0.901 | 0.005 | 0.026 |
| 出口 3 | 0.001 | 0.012 | 0.913 | 0.007 |
| 出口 4 | 0.001 | 0.005 | 0.011 | 0.931 |

以下原生场图、采样结构图或 GUI 动画保留栅格格式；不把 PNG/GIF 嵌入 SVG 充当可编辑矢量图：

- `video/wdm-final-1270-GUI-XY-crop.gif`
- `video/wdm-final-1290-GUI-XY-crop.gif`
- `video/wdm-final-1310-GUI-XY-crop.gif`
- `video/wdm-final-1330-GUI-XY-crop.gif`

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
