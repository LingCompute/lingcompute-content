# 功率分配：来源与证据

本系列用示意、解析模型和本项目已完成的 FDTD 求解解释器件。来源清单不是同条件性能排名，也不代表把第三方 Notebook、几何或原始数据按本库许可重新分发。

## 官方案例

- [Waveguide Y junction](https://www.lingcompute.com/photon/learning-center/examples/notebooks/YJunction)
- [Directional coupler](https://www.lingcompute.com/photon/learning-center/examples/notebooks/DirectionalCoupler)
- [2×2 MMI power splitter](https://www.lingcompute.com/photon/learning-center/examples/notebooks/MMIPowerSplitter2x2)：第 1、2 篇的三类结构几何示意来源；第 3 篇沿用其已建模器件、材料与窄端输入设置，另做本项目的三项逐模 FDTD 实验。
- 定向耦合器几何参考：[官方 coupler.gds](https://github.com/flexcompute/tidy3d-notebooks/blob/develop/misc/coupler.gds)。

## 数值口径

**Y 分支**：约 1.55 μm，输入功率归一化的前向基模总透射约 97.0%，1.53–1.57 μm 约 96.6%–97.0%。只在上支路保存模式监视器，另一支路由镜像对称推得；50∶50 是两路内部的分配，不等于每路收到输入功率的一半，也不是两路独立实测。场图为频域总 `|E|²`。

**定向耦合器**：硅波导、二氧化硅衬底、空气上包层；名义宽 450 nm、间距 100 nm、平行段约 4.0 μm，厚 220 nm，`dilation=20 nm`、底面参考、侧壁角 30°。底面实际宽约 490 nm、间距约 60 nm，不能把名义尺寸当作全高截面。1.5505 μm 的交叉/直通前向基模功率相对源约 59.3%/39.5%，总和约 98.8%；60∶40 的分母是两路之和。1.53–1.57 μm 内保存三个离散点，不代表连续带宽已充分采样。相位采用当前输出模式基底和 `x=8 μm` 参考面，改变约定可能改变相位符号。

正文的 `κ_eff≈0.2215 μm⁻¹` 是单点、最短反正弦分支的完整器件等效标定；`γ≈7.75 μm⁻¹` 来自指定折射率的解析示例。参考长度和间距灵敏度图为理想模型换算，不是长度或间距扫描仿真。输入归一化透射、输出占比和相位需一起解读。

### 第 3 篇 MMI 的数值与实验口径

**原窄端输入案例**（本系列原有的 FDTD 结果）：硅 220 nm 厚、二氧化硅衬底、空气上包层，核心 3.0 × 1.0 μm，λ = 1.55 μm；输入为 0.4 μm 窄波导基模，接入位置 y = +0.3 μm；两个输出模式监视器位于 S 弯之后。1.55 μm 处两路前向基模功率为源功率的 41.44% 与 43.95%，合计 **85.4%**；按两路之和归一化得 **48.5∶51.5**。1.53–1.57 μm 窗口内只有 5 个离散采样点，上路占比 44.4%–53.0%，两路基模总透射 84.5%–87.8%；图 5 的线条只连接采样点，不代表连续带宽已充分采样。85.4% 只计两路前向基模，未把余量完整分解为反射、其他模式和辐射。

**实际截面矢量模式求解**：1.0 μm × 220 nm 硅/SiO₂ 截面，λ = 1.55 μm，得到 3 个 TE-like 导模，n<sub>eff</sub> = 2.743087 / 2.417316 / 1.816538，另有 2 个 TM-like 导模。模式网格由每波长 20 点加密至 28 点，三个 TE-like 的 n<sub>eff</sub> 相对变化约 0.099% / 0.103% / 0.037%；这只是截面模式求解的网格核对，**不代表完整器件的 FDTD 已做网格收敛验证**。按前两阶计算 L<sub>π,矢量</sub> = λ/[2(n<sub>eff,0</sub> − n<sub>eff,1</sub>)] ≈ 2.37897 μm，加密后约 2.37739 μm（变化约 0.07%）。正文的 3.5 μm 是 TE 平板基模加侧向穿透修正的解析估值（n<sub>r</sub> ≈ 2.85、W<sub>e</sub> ≈ 1.2 μm），只作为长度标度；图 3 的四个标量模式与图 4 的 W<sub>e</sub>²/λ 标度都是理想模型示意，不是本器件的模谱或扫描结果。

**三项逐模 FDTD 实验**（本项目新增，激励条件与上面原案例不同）：保持原结构、材料、3.0 × 1.0 μm 核心与两侧 S 弯不变，把模式源放在宽区内部 x = −1.2 μm（距核心左界面 0.3 μm、距右界面 2.7 μm），分别馈入 TE-like 0、1、2；每次只改激励模式。频域 FieldMonitor 记录 1.55 μm 的场，FieldTimeMonitor 记录 z = 0 中面 Ey 的真实时序（约 0.507 fs 间隔，xy 每 2 点取样），核心与两路输出各放 ModeMonitor。两路前向基模功率之和相对各任务源功率为 **0.71538 / 0.97203 / 0.23438**（正文取 71.5% / 97.2% / 23.4%），两路基模分光比均约 50∶50；器件关于 y = 0 镜像对称、单模有确定奇偶性，故两路基模近等强。核心监视器里目标模式占已存前向模式功率均 > 99.9%，这是激励纯度，不是转换效率。三项独立实验的输出功率不能简单相加或平均来复现原案例的相干组合输入；两路基模之外的余量未单独归为辐射损耗。逐模实验**没有做长度扫描**，也不用于给出原案例的 48.5∶51.5 或 85.4%。

## 随文素材逐项说明

| 文件 | 制作与解释边界 |
| --- | --- |
| `figures/01-application.svg` | 本项目原创应用解释图，线长和亮度不表示功率 |
| `figures/03-metrics.svg` | 本项目教学图，数字为人为示例，不是仿真 |
| `figures/02-three-families.svg` | 从三个官方案例对应模型提取几何后由本项目绘制，缩略图比例不统一 |
| `figures/04-y-junction.png` | 本项目 FDTD 结果重绘，约 1.55 μm，频域总 `\|E\|²` |
| `figures/12-supermode.svg` | 双高斯峰构造的偶奇场教学示意，不是实际截面的数值超模 |
| `figures/11-coupler-length.svg` | 理想无损、相位匹配模型的解析功率曲线 |
| `figures/13-mismatch.svg` | 固定 κ 改变 Δβ 的解析示例，不是几何扫描 |
| `figures/15-sensitivity.svg` | 单点标定及指数间距示例，不是间距扫描 FDTD |
| `figures/05-directional-coupler.png` | 本项目 FDTD 结果重绘，约 1.5505 μm，频域总 `\|E\|²` 与同模型介电结构 |
| `figures/14-validation.svg` | 读取本项目两端基模复振幅，功率占比与相对相位；直通占比低于 1% 的点标灰 |
| `video/YJunction-GUI-3D-crop.gif` | 同名无 `-crop` GUI 原生导出件经裁剪、缩放、补白和量化；Re(Ey)，约 1.55 μm |
| `video/DirectionalCoupler-GUI-3D-crop.gif` | 同上；Re(Ey)，约 1.55049 μm |
| `figures/06-mmi.png` | 原窄端输入案例的 FDTD 频域场强 \|E\|²，按监视器真实非均匀网格重采样后绘制；场监视器只覆盖多模区核心段 |
| `figures/20-mmi-vector-modes.png` | 本项目本地矢量模式求解的源截面 Re(Ey) 与 z = 0 横向剖面，各模式分别归一化；原生栅格场图，不是 FDTD 传播结果 |
| `figures/16-mmi-phase.svg` | 理想平板模型的解析相位盘与场叠加示意；四个标量模式只解释自成像关系，不代表实际三模谱 |
| `figures/18-mmi-ruler.svg` | 器件俯视轮廓与 W<sub>e</sub>²/λ 解析标度示意；约 3.5 μm 为平板近似估值，不是 FDTD 扫描 |
| `figures/19-mmi-spectrum.svg` | 原窄端输入案例 FDTD 的 1.50–1.61 μm 离散采样点，线条只连接采样点 |
| `video/MMI-modes-FDTD-comparison.gif` | 三项逐模 FDTD 结果的同步对照；前 16 秒为真实时域 Ey 记录（0–236.26 fs），后 8 秒为 1.55 μm 频域场的相位循环，不表示脉冲传播。由本项目已有 24 秒 MP4 转码：720×960、10 fps、240 帧、128 色、无限循环 |
| `video/MMIPowerSplitter2x2-GUI-3D-crop.gif` | 原案例 GUI 原生导出的 2×2 MMI 3D Carpet 动画，经裁剪、缩放与量化；Re(Ey)，1.55 μm。起伏是单频场相位变化，不是结构形变或脉冲传播 |
| `qr/03-mmi.png` | 本项目按公开案例 URL 生成的二维码，用于公众号稿页尾案例卡；不含私人链接或凭据 |

示意图与数据图以 SVG 为随文源图，由本地 matplotlib 脚本生成：导出后去掉 DOCTYPE、`metadata` 与全局样式表，把 `*{stroke-linejoin…}` 提升为根元素展示属性，样式写成展示属性，文字保留为 `<text>` 而不转轮廓。第 3 篇的 `16-mmi-phase.svg`、`18-mmi-ruler.svg`、`19-mmi-spectrum.svg` 同样为可编辑 SVG，文字使用小米 MiSans（Regular / Medium / Semibold）；字体文件不入库、不随图分发。公众号上传副本由构建从 SVG 渲染生成，不单独维护。仿真场图与模式场图（`04-y-junction.png`、`05-directional-coupler.png`、`06-mmi.png`、`20-mmi-vector-modes.png`）是原生栅格：场按监视器真实网格重采样后绘制，避免非均匀网格被线性拉伸而与器件轮廓错位；场图不做 PNG 套壳成 SVG。

两类 GIF 不同：`YJunction-` 与 `DirectionalCoupler-` 及 `MMIPowerSplitter2x2-` 开头的裁剪版来自 GUI 原生 3D Carpet 单频场导出，起伏表示场值，不是器件形变或脉冲传播，裁剪版不保证完整底部色标；`MMI-modes-FDTD-comparison.gif` 是本项目三项 FDTD 结果的渲染转码，前段是真实时域记录、后段是单频场相位循环，两段的口径在正文图注中分开写出。定量读数以正文及静态结果为准。没有把第三方现成 PNG 当成本项目重绘。

## 权利范围

原创文字与原创解释图适用本库 CC BY-NC 4.0。官方案例、几何、产品界面及其可能包含的第三方权利保留原条件；本项目结果图和 GUI 导出不向读者授予这些底层第三方材料的新许可。随文 GIF（`MMIPowerSplitter2x2-GUI-3D-crop.gif`）沿用 GUI 导出件的既有边界；新增逐模 FDTD 的场图与动图由本项目自行求解、绘制和转码，不把云端任务标识、费用记录或求解凭据写进公开稿。原始 Notebook、GDS、求解数据与 GUI 原件不随本系列分发，审核需要时由维护者另行提供核查。

本系列第 3 篇使用的二维码为按公开案例 URL 自行生成，不含私人链接、账号或凭据；公众号载体图（关注横幅、签名卡、阅读原文条）与品牌标识仍按仓库 `docs/rights.md` 处理，未重绘或二次编码。

可核查[产品条款](https://www.flexcompute.com/terms-of-use/)与[官方结果下载/查看说明](https://www.flexcompute.com/tidy3d/learning-center/faq/)。公开条款未在本次核查中提供覆盖所有输出及 GUI 元素的明确再许可条款，不能将“可下载”视为可以向第三方授予 CC 许可。需要重用这些素材时请另核实适用协议和相应权利；本页不作法律判断。

前两篇历史审核状态和初始文件哈希见仓库 `reviews/legacy.json`；第 3 篇为新增待审稿，按内容 PR 流程由指定业内审核者批准当前提交后才收录。原始制作材料保留于制作方，审核需要时由维护者安排核查。
