# 待审证据记录：不写几何，只写目标

状态：技术、逐图来源和授权待人审。作者 GitHub 账号尚未提供，`authors` 留空，不得据此安排作者自审。原稿只做待审标识和目录适配，未重新求解或核验数值。

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
| `figures/11-design-region.png` | 图 1：设计区与端口。4.5×4.5 μm 的方块被切成 300×300 个像素，每个像素的填充率都是优化变量。示意，颜色不代表真实优化结果。 |
| `figures/12-objective.png` | 图 2：目标函数的四层结构。前两层管光学性能，第三层管可制造性，第四层管通道均衡。 |
| `figures/17-wdm-convergence.png` | 图 3：目标函数随迭代的变化。前 1/3 只提透射，之后加入串扰惩罚，曲线出现一次台阶。本次运行，2D，50 步。 |
| `figures/18-wdm-spectra.png` | 图 4：四个出口的透射谱。每个口在自己对应的波长上出现峰值，其余波长被压低。本次运行，151 点采样。 |
| `figures/19-wdm-matrix.png` | 图 5：通道功率矩阵。行是出口，列是通道，数值为通道带宽内 5 点平均功率。本次运行。 |
| `video/wdm-final-1270-GUI-XY-crop.gif` | 动画 1：本次 FDTD 末态的 1270 nm XY 场，GUI 原生导出，Re(Ez)。对应 mode_0 出口，y = −1.6875 μm。 |
| `video/wdm-final-1290-GUI-XY-crop.gif` | 动画 2：本次 FDTD 末态的 1290 nm XY 场，GUI 原生导出，Re(Ez)。对应 mode_1 出口，y = −0.5625 μm。 |
| `video/wdm-final-1310-GUI-XY-crop.gif` | 动画 3：本次 FDTD 末态的 1310 nm XY 场，GUI 原生导出，Re(Ez)。对应 mode_2 出口，y = +0.5625 μm。 |
| `video/wdm-final-1330-GUI-XY-crop.gif` | 动画 4：本次 FDTD 末态的 1330 nm XY 场，GUI 原生导出，Re(Ez)。对应 mode_3 出口，y = +1.6875 μm。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`dfccec935f6655cdb4367ad6ef5dbd2af5a155b1192560df53db17268e1c0971`。
