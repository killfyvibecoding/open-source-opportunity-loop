# 开源机会 Loop

> 把一个模糊想法，转化成清晰的业务切口、可复用的开源底座、可验证的 MVP 和下一步行动。

[English README](README.md)

## 这是什么

开源机会 Loop 是一个可复用的 Codex Skill，采用“对话优先”的方式工作。

用户只需要说一句：

> 我想做一个面向陶瓷出口企业的 AI 内容系统。

Skill 就会自动完成：

- 判断当前是在定位、检索、核验、组合、商业验证还是继续推进；
- 当想法模糊时，先把技术能力转换成具体的付费业务切口；
- 找到可以复用或组合的开源项目；
- 搜索 AI 模型、数据集、RAG 和 Agent 能力；
- 检查许可证、活跃度、部署难度和第三方依赖；
- 参考独立开发产品和市场案例；
- 输出 7 天 MVP、30 天产品和私有部署路线；
- 给出可验证的变现假设和下一步行动。

它不是简单的开源项目列表，而是一个“从想法到产品决策”的 Loop。

## 核心流程

```text
用户想法
  ↓
状态识别与意图路由
  ↓
问题澄清与产品定位
  ↓
开源项目发现与组合
  ↓
技术、许可证和商业闸门
  ↓
一个可执行产物
  ↓
用户反馈 → 动态选择下一步
```

Skill 不要求用户记住内部模块。直接说“我想做什么”即可；如果上一轮已经有结果，直接说“继续”，它会基于当前状态推进一个最重要的下一步。

## 基础资料库

本 Skill 使用以下四个资料库作为基础知识层：

- [sindresorhus/awesome](https://github.com/sindresorhus/awesome)：广泛的开源技术索引；
- [Programmer Edition](https://github.com/1c7/chinese-independent-developer/blob/master/pages/README-Programmer-Edition.md)：独立开发者项目；
- [2018–2020](https://github.com/1c7/chinese-independent-developer/blob/master/pages/README-2018-2020.md)：历史项目和长期验证信号；
- [Game](https://github.com/1c7/chinese-independent-developer/blob/master/pages/README-Game.md)：游戏、流量和游戏变现案例。

## 其他来源

根据问题类型，Skill 还会查询：

- GitHub Trending、Awesome Selfhosted、HelloGitHub；
- OpenResource、Open Source Atlas、Gitee；
- Hugging Face、Papers With Code；
- `awesome-agents`、`awesome-llm-apps`；
- Libraries.io、LFX Insights；
- 阿里开源、字节跳动开源、Apache、Eclipse；
- Indie Hacker Projects、Product Hunt、Indie Hackers、IndieTools。

完整来源和用途见 [references/source-catalog.md](references/source-catalog.md)。

## 使用方式

将仓库复制到你的 Agent 使用的 Skills 目录，然后调用：

```text
$open-source-opportunity-loop
```

示例：

```text
使用 $open-source-opportunity-loop。
我想做一个面向中国陶瓷外贸企业的 AI 内容系统，帮我找开源底座，检查 License，给出 7 天 MVP 和变现方案。
```

```text
使用 $open-source-opportunity-loop。
我想给建材厂做一个 AI 和视频系统，但方向很模糊，先帮我清晰定位。
```

```text
使用 $open-source-opportunity-loop。
找 10 个可以在 30 天内改造成 B2B SaaS 的开源项目，并说明哪些可以直接商用。
```

```text
使用 $open-source-opportunity-loop。
把这些开源项目组合成一个适合中国制造业的 AI 产品，给出技术路线、客户和收费方式。
```

## 标准输出

每次推荐应包含：

1. 当前路由、需求理解和关键假设；
2. 证据缺口和必要问题；
3. 直接底座、模块、AI 能力和市场参考；
4. License、维护、部署和区域适配风险；
5. 一个推荐路线及对应产物；
6. 一个最重要的下一步验证实验。

只有当用户进入相应阶段时，才展开 7 天 MVP、30 天产品或私有部署路线。

## 目录结构

```text
SKILL.md                         Skill 核心流程
agents/openai.yaml               Skill 展示和调用信息
references/                      来源、搜索、许可证和变现规则
examples/                        具体业务和续接 Loop 示例
scripts/validate_skill.py        无第三方依赖的结构验证脚本
.github/                         CI、Issue 和 PR 模板
```

## 许可证与注意事项

本仓库使用 [MIT License](LICENSE)。但本 Skill 推荐的第三方项目、模型、数据集、字体、图片和商标都有各自的授权条件，不能因为被收录或被推荐就默认可以商用。

使用前必须回到原项目仓库核对 License 和 Notice。这个 Skill 提供的是实用研究建议，不构成法律、财务或合规意见。

Skill 不会要求用户在对话中粘贴 GitHub Token。需要 GitHub 权限时，请使用本机 `gh auth login` 或受保护的环境变量。

本 Skill 的动态路由设计参考了 [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) 的公开交互思路，但没有复制其代码、原文、知识库、素材或模板。相关边界见 [inspiration-and-boundaries.md](references/inspiration-and-boundaries.md)。

## 贡献

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，并在提交前运行：

```bash
python3 scripts/validate_skill.py
```

## 相关文档

- [来源目录](references/source-catalog.md)
- [动态路由](references/interaction-router.md)
- [搜索流程](references/search-workflow.md)
- [许可证与项目健康度](references/license-and-health.md)
- [变现手册](references/monetization-playbook.md)
- [状态与反馈](references/state-and-feedback.md)
- [启发与授权边界](references/inspiration-and-boundaries.md)
