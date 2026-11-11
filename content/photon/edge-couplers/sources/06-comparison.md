# 待审证据记录：端面接口怎么选：先定波段，再定面积，最后才比 dB

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
| `figures/18-compare.svg` | 图 1：四个案例的扫描窗口。倒锥与模斑转换为 1500–1600 nm，双层 SiN 为 400–640 nm，自由曲面为 650–1050 nm。 |
| `figures/13-wsc-loss.svg` | 图 3：线性锥、Luneburg 和半透镜的总通量谱。前两者收束、后者扩束，厚度与端口条件不同。 |
| `figures/27-loss-length.svg` | 图 4：器件长度与设计点损耗。长度与损耗之间没有单调关系——最长的双层 SiN 损耗最高，最短的模斑转换损耗最低。 |
| `figures/19-choice.svg` | 图 2：按界面位置、波段、面积三个问题走，大多数项目能落到一个答案上。 |
| `figures/02-tolerance.svg` | 图 5：两个假设高斯模式的横向偏移损失，仅说明模场尺寸影响，不提供接口容差保证。 |

SVG 与保留的 PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`bb02ad3be9093542227516285c97281382a89cbd83a8e674fc40aa9a53352860`。

编辑更正（2026-11-11）：将正文比较表前的“本次实测”改称“本次仿真”，与各案例的求解来源一致；数值与待审状态不变，本次未重新求解。

## 可编辑图片迁移（2026-11-11）

本篇示意图、流程图和曲线图以 SVG 作为发布源图，正文直接引用。复用原制作工程的矢量几何、曲线与文字，去掉 DTD、非视觉元数据和全局样式；文字保留为 `text` / `tspan`，统一使用 MiSans（小米）Regular、Medium、Semibold，字重为 400、500、600。字体来源及许可见[字体说明](../../../../docs/rights.md#字体)。原始字体文件不随源图分发，HTML 共用构建工具嵌入的官方原字库。图内排版按手机参考宽度复核，数值、单位、归一化与审核边界仍按本篇证据记录。

| SVG 源图 | 迁移前 PNG SHA256 | 原工程 SVG SHA256 |
| --- | --- | --- |
| `figures/18-compare.svg` | `a9727ac01d5ec3b0a47945a807ff8e8fa47e3337c774c4fe763013f1ea47b5cd` | `7a915d0b43a9dad5abac72e2d49ab3beca3ff48fe571655492e3e37ba9c13e39` |
| `figures/13-wsc-loss.svg` | `f7f25a80ebd2e2a39f310785c42a21b2b37875fcf4737e70475cfb42002814df` | `7a683fbbfecd0da042398818afb300773c31c6b7efb8fcbf135fbd87782968f9` |
| `figures/27-loss-length.svg` | `1bc5ee41dcd595ee9115b87303571b94975e8b872ba27541f130f74914f2746b` | `01e4fb9b4bcadfc8fb153cf5bfb1c13f19f9ad13daa486b6d287cb84908c40f4` |
| `figures/19-choice.svg` | `c78157de01e3d42e592fed4d4c4747274f2f7ab07451ce812dbb71b336ff3cae` | `c486f8cdfe9f83e1ac208589066efc0f6b23e5ab20c2610158723a57c4a78e85` |
| `figures/02-tolerance.svg` | `61ce121aed841fc1301ef70e68ee11357590f0a8c7f1506d050f09efa32bf4a7` | `ee0e394c40d9fbdbe17120bad084e25706bc24e4a675a0675e80d2e06efa8e35` |

公众号需要的 PNG 上传副本及手机长图由完整构建从 SVG 生成，仅留在忽略的 `build/`。SVG 原图与上传副本的路径、哈希均由素材清单记录。格式迁移与自查不构成专业批准，本次新提交仍须指定非作者业内审核者批准。

## 本轮版面复核

按 MiSans 实际文字占位调整了标题、图注与内容区的间隔，并扩展画布以保留完整坐标和标签；曲线和数值保留原有口径。手机预览与公众号上传副本来自同一 SVG。排版复核不替代逐图技术审核，最小字号与理解难度还需目标读者在真机上试读。
