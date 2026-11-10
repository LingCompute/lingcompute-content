<img src="assets/brand/lingcompute-horizontal.svg" alt="灵算科技 LingCompute" width="300">

# 灵算技术内容库

面向工程师、科研人员和学习者的灵算官方技术内容。按产品和系列阅读，每篇说明读者前提、原理、证据和适用条件。

## 按产品阅读

| 产品 | 文章 | 产品入口 |
| --- | --- | --- |
| 灵算光子 | [图解无源光子器件 · 功率分配](#图解无源光子器件--功率分配) | [产品介绍](https://www.lingcompute.com/products/photon) |
| 灵算流体 | 待首篇审核后收录 | [产品介绍](https://www.lingcompute.com/products/fluid) |
| 灵算射频 | 待首篇审核后收录 | [产品介绍](https://www.lingcompute.com/products/rf) |
| 灵算洞察 | 待首篇审核后收录 | [产品介绍](https://www.lingcompute.com/products/insight) |

### 图解无源光子器件 · 功率分配

适合具有光学基础、需要理解和选择集成光子器件的工程师与科研人员。

1. [一束光，怎么被“掰”成两路？](content/photon/power-splitters/01-y-junction.md) — 分清分光比和总透射，理解对称 Y 分支。
2. [两条波导靠得够近，光就自己换手](content/photon/power-splitters/02-directional-coupler.md) — 用超模和耦合模模型理解长度、失配与几何取舍。

[来源、定量口径与素材说明](content/photon/power-splitters/SOURCES.md)。两篇的当前版本已由项目负责人确认完成历史人审；审核者署名和实际日期未提供，记录见 [legacy.json](reviews/legacy.json)。后续篇目通过独立 PR 审核后逐篇收录。公开 PR 中的稿件仍是待审稿，正式目录以 `main` 为准；收录也不等于已经在公众号发送。

## 投稿与生成

人维护 Markdown 和随文素材；工具生成 HTML、手机截图、阅读时长和上传清单。技术结论由指定业内审核者审批，微信公众号最终发送由人操作。

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
python -m unittest discover -s tests
python tools/build.py --check
python tools/build.py
```

打开生成的 `build/index.html` 查看文章。CI 的 `article-preview` 附件包含相同产物；下载后在本地打开。生成目录不入库。投稿方式见 [CONTRIBUTING.md](CONTRIBUTING.md)，默认排版与篇幅见 [编辑规范](docs/editorial.md)，审核流程见 [审核规则](docs/review.md)。

| 目录 | 用途 |
| --- | --- |
| `content/<产品>/<系列>/` | Markdown、随文图与最小证据记录；主分支只收录已审内容 |
| `production/` | 投稿者可选择附带的制作材料，独立于文章审核 |
| `tools/`、`tests/` | 共享生成、检查与测试 |
| `assets/brand/` | 公司标识及单独的商标说明 |
| `build/` | 自动生成的预览和公众号排版材料 |

自有工具代码采用 [MIT](LICENSE)，自有文章和插图采用 [CC BY-NC 4.0](LICENSE-CONTENT.md)，允许署名的非商业转载和改编，商业使用另行授权。商标、产品界面及另有标注的第三方材料按[各自权利说明](docs/rights.md)处理。来源页面和产品功能可能更新，请以当前官方文档为准。
