# 待审证据记录：工业界为什么用阵列波导光栅？

状态：技术、逐图来源和授权待人审。作者 GitHub 账号尚未提供，`authors` 留空，不得据此安排作者自审。原稿只做待审标识和目录适配，未重新求解或核验数值。

## 来源入口

- https://www.lingcompute.com/photon/learning-center/example-library
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/Autograd9WDM
- https://www.lingcompute.com/photon/learning-center/examples/notebooks/MultiplexingMMI

以上同时包含原稿链接与系列候选参考；不表示本篇已经逐项复现所有案例。审核前需把每个定量结论与实际模型/推导对应。只有通用案例入口或缺少原稿来源链接的篇目，尤其需要补齐文章级依据。

## 条件与口径

MMI 的 EME 结果与逆向设计 FDTD 不作同条件排名；AWG/EDG 为机制说明，没有在本项目复现官方实例。目标函数、透射、串扰与带宽分别核查。

具体材料、波段、单位、归一化与采样条件见原稿相邻段落，需由审核者交叉核对。制作方保留原始工程，可安排审核者核查；原始数据、Notebook、日志与私人结果链接不在本 PR 公开。

## 随文素材

| 文件 | 原稿图注（待核查） |
| --- | --- |
| `figures/07-awg.png` | 图 1：AWG 结构。中间一排波导长度递增，相邻差 ΔL；两个自由传播区负责把光摊开、再收拢。机制示意，非本次仿真。 |
| `figures/08-grating-equation.png` | 图 2：ΔL 与 FSR 的关系，以及通道数受 FSR 限制的由来。机制说明，非本次仿真。 |
| `figures/09-edg.png` | 图 3：EDG 结构。一块平板波导加一侧的凹面反射光栅，输入与输出都在同一侧。机制示意，非本次仿真。 |
| `figures/10-area-tradeoff.png` | 图 4：AWG 与 EDG 的面积随通道数的定性走向。通道少时 EDG 省地，通道多时 AWG 反超。趋势示意，不是实测面积。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`963fd55160ce21e92a3e10d800861b60a36969a3afc2ef4d18f285ffd488a5e6`。

排版更正（2026-11-11）：将 1 个独立公式段标记为 `p.eq`，供统一排版与公式阅读计时；数学内容、数值和上下标不变，待审状态不变。
