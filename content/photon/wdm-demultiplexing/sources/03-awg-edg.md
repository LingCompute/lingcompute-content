# 待审证据记录：工业界为什么用阵列波导光栅？

状态：技术、逐图来源和授权待人审。作者 GitHub 账号为 `Frank-DingYC`（2026-11-11 人工确认），已同步 `authors`；须由非作者审核。原稿只做待审标识和目录适配，未重新求解或核验数值。

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
| `figures/07-awg.svg` | 图 1：AWG 结构。中间一排波导长度递增，相邻差 ΔL；两个自由传播区负责把光摊开、再收拢。机制示意，非本次仿真。 |
| `figures/08-grating-equation.svg` | 图 2：ΔL 与 FSR 的关系，以及通道数受 FSR 限制的由来。机制说明，非本次仿真。 |
| `figures/09-edg.svg` | 图 3：EDG 结构。一块平板波导加一侧的凹面反射光栅，输入与输出都在同一侧。机制示意，非本次仿真。 |
| `figures/10-area-tradeoff.svg` | 图 4：AWG 与 EDG 的面积随通道数的定性走向。通道少时 EDG 省地，通道多时 AWG 反超。趋势示意，不是实测面积。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`963fd55160ce21e92a3e10d800861b60a36969a3afc2ef4d18f285ffd488a5e6`。

排版更正（2026-11-11）：将 1 个独立公式段标记为 `p.eq`，供统一排版与公式阅读计时；数学内容、数值和上下标不变，待审状态不变。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/07-awg.svg` | `8f091c00aade54991bc016e304deef597fdb771f52c795e8f7fb140afc5436ca` | `ebdf8137eec5155b48e4975702d05fee2febbb9db7ae9748ce706082c8411a9d` |
| `figures/08-grating-equation.svg` | `fe5f8afed936d48add93a4e647a58d0a456473144baca463c193c6cd710c2eb3` | `60eb92ae8f3964c48ce700098768d61c3136e2b65bdb1a2ab91bf1440d521665` |
| `figures/09-edg.svg` | `933da2db70f47ea49128e5a8cf0c3c0ba23eabd9975ede96caa5199194683220` | `1eda1405ab3a8603bc84defb50cff19eff3fa5bdfa939020491b1b1ab809eee2` |
| `figures/10-area-tradeoff.svg` | `0302098fe3ba857e89ecf78be838c60300e07cd16cffcaf641bfd9e0f33d546f` | `34014781b81ea7eb4198eb533b53cb03cc35b715721ff95c1dc6b31535c4f30a` |

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。

`figures/10-area-tradeoff.svg` 另作定性示意重绘：原图把通道数 4–64 直接画入 0–10 画布，导致曲线与图例裁切。新图保留原图题的 AWG／EDG 占地趋势说明，使用无刻度曲线展示关系；交点、斜率与绝对面积均不代表任何仿真、量测或拟合，也不沿用原教学表达式作为定量证据。不得从这张图读取面积或选型阈值；这一趋势及适用边界仍须业内审核者核查。
