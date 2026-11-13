# 图解无源光子器件 · 光栅耦合器：来源与证据

本系列用示意、解析模型和本项目已完成的 FDTD 求解解释器件。来源清单不是同条件性能排名，也不代表把第三方 Notebook、几何或原始数据按本库许可重新分发。

## 官方案例

- [Grating coupler](https://www.lingcompute.com/photon/learning-center/examples/notebooks/GratingCoupler)：均匀线性光栅，第 1 篇引用的四指标来源。
- [Focused apodized grating coupler](https://www.lingcompute.com/photon/learning-center/examples/notebooks/FocusedApodGC)：聚焦切趾光栅，第 1 篇只引用其峰值量级。
- [Bilayer SiN/Si grating coupler](https://www.lingcompute.com/photon/learning-center/examples/notebooks/BilayerSiNSiGC)：双层 SiN/Si 光栅，第 1 篇只引用其峰值量级。
- 系列入口：[灵算光子学习中心](https://www.lingcompute.com/photon/learning-center/example-library)；国内产品入口 [tidy3d.fangzhen.cloud](https://tidy3d.fangzhen.cloud/)。

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
| `figures/01-interface.svg` | 本项目原创结构示意：端面耦合与光栅耦合两种入口，尺寸未按真实比例 |
| `figures/02-principle.svg` | 本项目原创教学示意：相位匹配与散射波叠加，不是仿真场 |
| `figures/03-metrics.svg` | 本项目数据图：四个指标定义 + 本次均匀光栅求解的四条功率去路（38% / 26% / 20% / 未分解 16%） |
| `figures/04-three-routes.svg` | 本项目原创结构示意：三条路线的设计自由度对照，齿宽与周期未按真实比例 |

示意图与数据图以 SVG 为随文源图，由本地 matplotlib 脚本生成：导出后去掉 DOCTYPE、`metadata` 与全局样式表，样式写成展示属性，文字保留为 `<text>` 而不转轮廓。文字使用小米 MiSans（Regular / Medium / Semibold）；字体文件不入库、不随图分发。公众号上传副本由构建从 SVG 渲染生成，不单独维护。场图与像素化结果保留原生栅格，不做 PNG 套壳成 SVG。

## 权利范围

原创文字与原创解释图适用本库 CC BY-NC 4.0。官方案例、几何、产品界面及其可能包含的第三方权利保留原条件；本项目结果图不向读者授予这些底层第三方材料的新许可。原始 Notebook、求解数据与 GUI 原件不随本系列分发，审核需要时由维护者另行提供核查；不把云端任务标识、费用记录或求解凭据写进公开稿。

## 待核查事项

第 1 篇为新增待审稿，按内容 PR 流程由 `config/reviewers.json` 中的光子领域审核者批准当前提交后才收录。需特别核查：三个案例的数值是否按上述口径复算一致；「不能直接排名」的限定是否在正文各处成立；四张图的文字与正文数字是否一一对应。
