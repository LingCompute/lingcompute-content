# 功率分配：来源与证据

本系列用示意、解析模型和本项目已完成的 FDTD 求解解释器件。来源清单不是同条件性能排名，也不代表把第三方 Notebook、几何或原始数据按本库许可重新分发。

## 官方案例

- [Waveguide Y junction](https://www.lingcompute.com/photon/learning-center/examples/notebooks/YJunction)
- [Directional coupler](https://www.lingcompute.com/photon/learning-center/examples/notebooks/DirectionalCoupler)
- [2×2 MMI power splitter](https://www.lingcompute.com/photon/learning-center/examples/notebooks/MMIPowerSplitter2x2)：仅用于三类结构的几何示意来源。
- 定向耦合器几何参考：[官方 coupler.gds](https://github.com/flexcompute/tidy3d-notebooks/blob/develop/misc/coupler.gds)。

## 当前两篇的数值口径

**Y 分支**：约 1.55 μm，输入功率归一化的前向基模总透射约 97.0%，1.53–1.57 μm 约 96.6%–97.0%。只在上支路保存模式监视器，另一支路由镜像对称推得；50∶50 是两路内部的分配，不等于每路收到输入功率的一半，也不是两路独立实测。场图为频域总 `|E|²`。

**定向耦合器**：硅波导、二氧化硅衬底、空气上包层；名义宽 450 nm、间距 100 nm、平行段约 4.0 μm，厚 220 nm，`dilation=20 nm`、底面参考、侧壁角 30°。底面实际宽约 490 nm、间距约 60 nm，不能把名义尺寸当作全高截面。1.5505 μm 的交叉/直通前向基模功率相对源约 59.3%/39.5%，总和约 98.8%；60∶40 的分母是两路之和。1.53–1.57 μm 内保存三个离散点，不代表连续带宽已充分采样。相位采用当前输出模式基底和 `x=8 μm` 参考面，改变约定可能改变相位符号。

正文的 `κ_eff≈0.2215 μm⁻¹` 是单点、最短反正弦分支的完整器件等效标定；`γ≈7.75 μm⁻¹` 来自指定折射率的解析示例。参考长度和间距灵敏度图为理想模型换算，不是长度或间距扫描仿真。输入归一化透射、输出占比和相位需一起解读。

## 随文素材逐项说明

| 文件 | 制作与解释边界 |
| --- | --- |
| `figures/01-application.png` | 本项目原创应用解释图，线长和亮度不表示功率 |
| `figures/03-metrics.png` | 本项目教学图，数字为人为示例，不是仿真 |
| `figures/02-three-families.png` | 从三个官方案例对应模型提取几何后由本项目绘制，缩略图比例不统一 |
| `figures/04-y-junction.png` | 本项目 FDTD 结果重绘，约 1.55 μm，频域总 `\|E\|²` |
| `figures/12-supermode.png` | 双高斯峰构造的偶奇场教学示意，不是实际截面的数值超模 |
| `figures/11-coupler-length.png` | 理想无损、相位匹配模型的解析功率曲线 |
| `figures/13-mismatch.png` | 固定 κ 改变 Δβ 的解析示例，不是几何扫描 |
| `figures/15-sensitivity.png` | 单点标定及指数间距示例，不是间距扫描 FDTD |
| `figures/05-directional-coupler.png` | 本项目 FDTD 结果重绘，约 1.5505 μm，频域总 `\|E\|²` 与同模型介电结构 |
| `figures/14-validation.png` | 读取本项目两端基模复振幅，功率占比与相对相位；直通占比低于 1% 的点标灰 |
| `video/YJunction-GUI-3D-crop.gif` | 同名无 `-crop` GUI 原生导出件经裁剪、缩放、补白和量化；Re(Ey)，约 1.55 μm |
| `video/DirectionalCoupler-GUI-3D-crop.gif` | 同上；Re(Ey)，约 1.55049 μm |

GIF 是 3D Carpet 单频场的相位变化演示，起伏表示场值，不是器件形变或脉冲传播。裁剪版不保证完整底部色标，定量读数以正文及静态结果为准。没有把第三方现成 PNG 当成本项目重绘。

## 权利范围

原创文字与原创解释图适用本库 CC BY-NC 4.0。官方案例、几何、产品界面及其可能包含的第三方权利保留原条件；本项目结果图和 GUI 导出不向读者授予这些底层第三方材料的新许可。原始 Notebook、GDS、求解数据与 GUI 原件不随首版分发。

可核查[产品条款](https://www.flexcompute.com/terms-of-use/)与[官方结果下载/查看说明](https://www.flexcompute.com/tidy3d/learning-center/faq/)。公开条款未在本次核查中提供覆盖所有输出及 GUI 元素的明确再许可条款，不能将“可下载”视为可以向第三方授予 CC 许可。需要重用这些素材时请另核实适用协议和相应权利；本页不作法律判断。

两篇历史审核状态和初始文件哈希见仓库 `reviews/legacy.json`。原始制作材料保留于制作方，审核需要时由维护者安排核查。


## 待审新增篇目：三种分光器，到底怎么选

[本篇来源、口径、素材与待核查项](sources/04-comparison.md)。指定业内审核者确认内容、来源及素材权利后才能收录。

本篇 4 张可编辑 SVG 源图及保留栅格素材的逐项说明，见[本篇迁移记录](sources/04-comparison.md#可编辑图片迁移2026-11-11)。
