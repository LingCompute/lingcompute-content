# 图解无源光子器件 · 光栅耦合器：来源与证据

本系列用示意、解析模型和本项目已完成的 FDTD 求解解释器件。来源清单不是同条件性能排名，也不代表把第三方 Notebook、几何或原始数据按本库许可重新分发。

## 官方案例

- [Grating coupler](https://www.lingcompute.com/photon/learning-center/examples/notebooks/GratingCoupler)：均匀线性光栅，第 1 篇引用的四指标来源。
- [Focused apodized grating coupler](https://www.lingcompute.com/photon/learning-center/examples/notebooks/FocusedApodGC)：聚焦切趾光栅，第 1 篇只引用其峰值量级。
- [Bilayer SiN/Si grating coupler](https://www.lingcompute.com/photon/learning-center/examples/notebooks/BilayerSiNSiGC)：双层 SiN/Si 光栅，第 1 篇只引用其峰值量级。
- 系列入口：[灵算光子学习中心](https://www.lingcompute.com/photon/learning-center/example-library)；国内产品入口 [tidy3d.fangzhen.cloud](https://tidy3d.fangzhen.cloud/)。

## 文献参照（第 1 篇「四条路」一节）

这一节只做入口方式的横向说明，数字用于判断量级，不是同条件对比；下表逐条给出出处与它原本的测量对象。

| 正文用法 | 出处 | 原始条件 |
| --- | --- | --- |
| 光纤模场直径 10.4 μm、硅波导截面 0.5 × 0.22 μm | 通信单模光纤与硅条波导的通用量级 | 1.55 μm 波段；模场直径按 SMF-28 类光纤取值，波导为几何截面而非模场尺寸 |
| 重叠效率 η = [2d₁d₂/(d₁²+d₂²)]²，0.5 μm → 0.9%（−20.4 dB） | 两个高斯模正对时的重叠积分，解析式 | **解析估计**，非仿真；真实模式非高斯，量级一致；不含反射与对准误差 |
| 端面耦合插损 1 dB 量级、带宽 > 100 nm | [Low-cost and high-efficiency single-mode-fiber interfaces to silicon photonic circuits](https://www.sciencedirect.com/science/article/abs/pii/S003040182030170X)（Optik, 2020） | 硅倒锥 + 三维聚合物模斑转换对接解理单模光纤，1550 nm，TE/TM 均约 −1.0 dB，PDL < 0.6 dB。属文献最好值，不代表通用工艺 |
| 单层均匀光栅 33%（−4.8 dB）、1 dB 带宽 40 nm、1 dB 额外损耗容差 2 μm | F. Van Laere 等，*Compact Focusing Grating Couplers for Silicon-on-Insulator Integrated Circuits*, IEEE PTL 19(23), 2007, [10.1109/LPT.2007.908762](https://doi.org/10.1109/LPT.2007.908762)（转引 Taillaert 等, JJAP 45, 2006） | SOI，1550 nm，近垂直入射；数值为该文引用的实验报道，不是本次求解结果 |
| 加底部反射镜后 69%（−1.6 dB） | 同上（转引 Van Laere 等, JLT 25, 2007） | 同上；反射镜为额外工艺层 |
| 45° 折转镜面为全反射、带宽与偏振不敏感 | F. Civitci 等, *Light turning mirrors for hybrid integration of SiON-based optical waveguides and photo-detectors*, Opt. Express 21(20), 2013, [10.1364/OE.21.024375](https://doi.org/10.1364/OE.21.024375) | SiON 平台，45° 准全反射镜；正文只引用机制，不引用其损耗数字（该文测的是对光电探测器的耦合，不是对光纤） |
| 光子引线键合 C 波段 1.6 ± 0.4 dB、1 dB 带宽 > 300 nm | N. Lindenmann 等, *Photonic wire bonding: a novel concept for chip-scale interconnects*, Opt. Express 20(16), 2012, [10.1364/OE.20.017667](https://doi.org/10.1364/OE.20.017667) | SU-8 聚合物波导，芯约 2 × 1.6 μm，两端 32 μm 长、尖端 20–100 nm 的倒锥；首代原型，非量产指标 |

口径说明：

- 正文的「偏离法线 10° 上下」是近垂直光栅的常见工作角；本系列第 2 篇的案例用 14.5°，属同一族但不在该区间内，两者不构成矛盾，也不可直接互相换算。
- 「对准容差比光栅小」是定性比较：端面耦合把模场撑到 2–3 μm，容差随模场尺寸缩小；本文不给端面耦合的容差数字，因为不同定义的报道差异过大。
- 第 1 篇正文出现的所有 dB 值要么来自上表文献，要么来自本系列自己的求解（后者见下一节）；两类数字在文中分别标注，不混算。

## 数值口径

**第 1 篇引用的均匀光栅读数**（本项目 3D FDTD 求解，高斯光束入射）：硅 260 nm、刻蚀 160 nm、填充因子 0.8、上包层 680 nm、BOX 2 μm，周期 0.62 μm、光纤位置 3.6 μm、倾角 14.5°、TE 偏振。1.55 μm 附近，前向基模耦合效率峰值 **−4.20 dB @1548 nm**（约 38%），1.55 μm 处 −4.23 dB；相对峰值的 3 dB 带宽 69 nm、1 dB 带宽 39 nm，两段均未触及扫描边界；衬底泄漏 26.3%；向上总反射 19.8%。

口径说明：

- 耦合效率取波导模式监视器 −x 方向基模的 |a|²，不是端面全部光功率。
- 衬底泄漏是下方通量监视器净通量占入射功率的比例，不等于材料吸收。
- 向上总反射是上方平面朝 +z 的净通量经源位置修正后除以入射功率，**不是**返回入射光纤模式的重叠功率，也不是波导反向基模反射；不能用它直接判断激光反馈强弱。
- 带宽相对峰值定义。三项已测功率合计约 84%，余项 16% 未作模式与辐射分解。
- 原 Notebook 只有模式监视器，本次另补 `field_xz`、`field_xy`、`flux_sub`、`flux_reflected` 四个监视器，因此效率与 Notebook 内嵌结果有微小差异（本次 −4.20 dB，Notebook 正文写 −4 dB）。

第 1 篇正文只把另两个案例的峰值当量级参照：聚焦切趾 −2.08 dB @1554 nm（正文写作「−2 dB 上下」）；双层 SiN/Si −2.00 dB @1539 nm 只在素材说明中登记，正文未给数字。它们的完整口径与条件随对应篇目给出。三个案例的材料模型、网格精度、监视器位置都不同，**不能当作同条件性能排名**。

## 随文素材逐项说明

| 文件 | 制作与解释边界 |
| --- | --- |
| `figures/01-mode-gap.svg` | 本项目解析估计图：两个高斯模正对时的重叠效率随芯片侧模场直径的变化，四个点为 0.5 / 2 / 3 / 10.4 μm；不是仿真场，不含反射与对准误差 |
| `figures/02-four-routes.svg` | 本项目原创结构示意：端面耦合、光栅耦合、45° 折转镜面、3D 打印桥接四种入口的几何对照，尺寸与齿宽未按真实比例 |
| `figures/03-principle.svg` | 本项目原创教学示意：相位匹配与散射波叠加，不是仿真场 |
| `figures/04-metrics.svg` | 本项目数据图：四个指标定义 + 本次均匀光栅求解的四条功率去路（38% / 26% / 20% / 未分解 16%） |
| `figures/05-three-routes.svg` | 本项目原创结构示意：三条路线的设计自由度对照，齿宽与周期未按真实比例 |

示意图与数据图以 SVG 为随文源图，由本地 matplotlib 脚本生成：导出后去掉 DOCTYPE、`metadata` 与全局样式表，样式写成展示属性，文字保留为 `<text>` 而不转轮廓。文字使用小米 MiSans（Regular / Medium / Semibold）；字体文件不入库、不随图分发。公众号上传副本由构建从 SVG 渲染生成，不单独维护。场图与像素化结果保留原生栅格，不做 PNG 套壳成 SVG。

`01-mode-gap.svg` 的曲线由 η = [2d₁d₂/(d₁²+d₂²)]² 在 d₂ = 0.42–12 μm 上直接计算；四条标注与正文的 −20.4 / −8.6 / −5.5 / 0 dB 由同一式代入得到，可逐点复算。`02-four-routes.svg` 只表达"光从哪个面进出、靠什么机制拐弯"，不承载任何尺寸或效率读数。

## 第 3 篇：聚焦切趾设计与仿真

- [FocusedApodGC 官方案例](https://www.lingcompute.com/photon/learning-center/examples/notebooks/FocusedApodGC)提供逐齿公式、圆弧版图与扫描方法。[Flexcompute 镜像](https://www.flexcompute.com/tidy3d/examples/notebooks/FocusedApodGC/)列出 70–140 nm 刻蚀深度（8 点）、0.015–0.035 μm⁻¹ 切趾斜率（6 点）、4–6 μm 光源位置（5 点）。约 −1.9 dB 为官方 2D 报告值。本项目 3D 使用光源位置参数 5.0 μm，按本地输入记录给出，官方页面部分版本的输出单元显示 5.500 μm。
- [Marchetti 等，Sci. Rep. 7, 16670 (2017)](https://doi.org/10.1038/s41598-017-16505-z)支持联合设计填充比例、局部周期和刻蚀深度；本文未把论文的器件性能用作本案例结果。[Zhao 与 Fan，JLT 38, 4435–4446 (2020)](https://arxiv.org/html/2002.05885)支持从目标辐射包络求散射强度，再用均匀光栅建立散射强度与几何映射。两齿尺寸表为公式演算，2.80 和 2.40 是说明算法用的假设值。
- 本项目既有的聚焦切趾 3D 入耦合求解基于 SOI，硅 220 nm、刻蚀 90 nm、上包层二氧化硅 780 nm、BOX 2 μm，R = 0.031 μm⁻¹，光源位置参数 5.0 μm，空气侧倾角 14.5°，TE 高斯束，模场直径 10.4 μm。波长按 1520–1580 nm、1 nm 间隔采样。耦合效率读 `mode_monitor` 的 −x 基模功率，以入射功率为基准。峰值 −2.08 dB @1554 nm，1550 nm 处为 −2.13 dB；`flux_sub` 与 `flux_reflected` 分别得到 26.5% 净下行通量和 11.2% 向上总反射，后者采用入射源修正、未做返回光纤模式投影。功率余量约 1%，未作完整闭面分解。1 dB 带宽按相对峰值的连续采样区间给出，3 dB 带宽下限受扫描窗限制。均匀光栅对照见上节，两例不能用于隔离切趾增益。另一次波导基模出耦合求解在 1550 nm 的源后逆向净通量约 1.72%（`flux_back`，相对入射功率），未拆分反向波导基模，故不作为模式反射率。

| 第 3 篇素材 | 来源、制作与授权 |
| --- | --- |
| `figures/10-apodized-principle.svg` | 沿用本项目 matplotlib 原创建模示意，保留 MiSans 可编辑文字，按 CC BY-NC 4.0。几何未按实际比例。 |
| `figures/12-apodized-field.png` | 沿用本项目 1550 nm FDTD 入耦合结果的俯视与剖面电场幅值图。对数色标与坐标沿用既有导出，保留原生栅格。 |
| `video/FocusedApodGC-GUI-3D-crop.gif` | 本项目入耦合结果的 Tidy3D GUI 原生 3D Carpet 导出并裁去界面边缘。固定 z 的 `field_xy` 单频 Re(Ey) 随相位变化，产品界面及其标识保留原有权利。 |
| `figures/11-apodized-spectrum.svg` | 沿用本项目 matplotlib 原创数据图，保留 MiSans 可编辑文字；左为模式功率，右为通量监视器结果，数据来自同一次 3D 入耦合求解。 |
| `qr/03-apodized.png` | 本项目预制案例二维码，已解码核对到灵算学习中心的 FocusedApodGC 页面。二维码和品牌标识保留相应权利。 |

第 3 篇沿用本地原稿随附图件及动图。SVG 字体使用小米 [MiSans](https://hyperos.mi.com/font/en/download/)，随文图未嵌入字库。论文只引用设计方法，未复制原图。原始仿真资料由维护者按需提供审核。

## 权利范围

原创文字与原创解释图适用本库 CC BY-NC 4.0。官方案例、几何、产品界面及其可能包含的第三方权利保留原条件；本项目结果图不向读者授予这些底层第三方材料的新许可。原始 Notebook、求解数据与 GUI 原件不随本系列分发，审核需要时由维护者另行提供核查；不把云端任务标识、费用记录或求解凭据写进公开稿。

## 待核查事项

第 1 篇为新增待审稿，按内容 PR 流程由 `config/reviewers.json` 中的光子领域审核者批准当前提交后才收录。需特别核查：三个案例的数值是否按上述口径复算一致；「不能直接排名」的限定是否在正文各处成立；五张图的文字与正文数字是否一一对应；「四条路」一节引用的文献数字是否按上表条件转述、没有把不同平台的读数并列成排名。
