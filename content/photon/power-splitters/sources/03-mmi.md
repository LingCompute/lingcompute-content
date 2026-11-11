# 待审证据记录：让一束光，在宽波导里自己干涉成像

状态：技术、逐图来源和授权待人审。作者 GitHub 账号尚未提供，`authors` 留空，不得据此安排作者自审。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/examples/notebooks/MMIPowerSplitter2x2
- https://www.lingcompute.com/photon/learning-center/example-library
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/YJunction
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/DirectionalCoupler

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

MMI 端口占比以两路之和归一化，总透射以输入源归一化；三类器件的材料、端口与采样条件不同，不构成同条件排名。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/06-mmi.png` | 图 1：2×2 MMI 的 FDTD 仿真场图。颜色表示频域场强 ／E／²，多模区的空间分布体现了模式间的干涉。 |
| `figures/16-mmi-phase.png` | 图 2：解析相位示意，绘出 m = 1–4 相对基模的相位差并对 2π 取余。在 3Lπ 处奇模反相、偶模同相，得到镜像单像；在 6Lπ 处全部同相，得到同向单像。 |
| `video/MMIPowerSplitter2x2-GUI-3D-crop.gif` | 动图 1：2×2 MMI 的 3D Carpet 动画。Re(Ey)，λ = 1.55 μm；展示单频场随相位变化的分布，起伏表示场值，并非结构形变或脉冲传播。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`cba7fd7ddd3607856be7ab8bfb79454731bf7b4d415fb8312fd541ba64793579`。

排版更正（2026-11-11）：将 4 个独立公式段和 1 个数值代入段标记为 `p.eq`，供统一排版与公式阅读计时；数学内容、数值和上下标不变，待审状态不变。
