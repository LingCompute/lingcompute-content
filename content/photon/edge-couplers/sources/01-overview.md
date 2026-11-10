# 待审证据记录：光怎么从芯片边缘进出？先把两种接口分清

状态：技术、逐图来源和授权待人审。作者 GitHub 账号尚未提供，`authors` 留空，不得据此安排作者自审。原稿只做待审标识和目录适配，未重新求解或核验数值。

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
| `figures/01-interfaces.png` | 图 1：两种接口的方向。左为面外（光栅），光被折出表面；右为面内（端面），光沿芯片平面直接进出。 |
| `figures/02-tolerance.png` | 图 2：两个假设高斯模场的偏移重叠。w 为束腰半径；曲线仅说明模场尺寸的影响，不代表两类接口的实测容差。 |
| `figures/03-four-routes.png` | 图 3：四种接口或模场转换案例。倒锥靠缓变轮廓；双层 SiN 用薄层接光、厚层布线；透镜型转换调整波前；自由曲面用反射面改变光路。 |
| `figures/11-edge-spectrum.png` | 图 4：倒锥的高斯光束到输出基模耦合谱。后续案例会分别说明自己的功率口径。 |
| `figures/12-wsc-fields.png` | 图 5：三种模斑转换方案的场分布。长度差三倍以上，机制也完全不同。 |

PNG/GIF 来自原制作工程；图注不是来源链或许可证明。合并前逐项确认示意/解析/仿真分类、原始案例、制作或裁剪关系、第三方权利条件。GUI 动画若为单频相位展示，不解释成脉冲传播；公司及第三方标识不纳入内容 CC 许可。本 PR 的公开审阅不授予额外的第三方权利。

原稿指纹（加入待审标识之前的 SHA256）：`d598254c42b9ff2b68a9ca0bf1fd4054e09314c0e46cc0c73761be386b775361`。
