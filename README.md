# Open Source Opportunity Loop 🔁

[![GitHub stars](https://img.shields.io/github/stars/killfyvibecoding/open-source-opportunity-loop?style=flat-square)](https://github.com/killfyvibecoding/open-source-opportunity-loop/stargazers)
[![License](https://img.shields.io/github/license/killfyvibecoding/open-source-opportunity-loop?style=flat-square)](LICENSE)
[![Validate Skill](https://github.com/killfyvibecoding/open-source-opportunity-loop/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/killfyvibecoding/open-source-opportunity-loop/actions/workflows/validate-skill.yml)

**简体中文** | [English](#english)

## 简体中文

> 把一个产品想法，转化成可复用的开源底座、可验证的 MVP 和具体的商业化路径。

## 这是什么

Open Source Opportunity Loop 是一个可复用的 Codex Skill，采用“对话优先”的方式工作。

用户只需要说一句：

> 我想做一个面向陶瓷出口企业的 AI 内容系统。

Skill 就会自动完成：

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
需求结构化
  ↓
开源项目发现
  ↓
技术、许可证和活跃度核验
  ↓
项目组合
  ↓
市场和变现验证
  ↓
MVP 与商业化方案
  ↓
用户反馈和下一轮推荐
```

## 基础资料库

本 Skill 使用以下四个资料库作为基础知识层：

- [sindresorhus/awesome](https://github.com/sindresorhus/awesome)：广泛的开源技术索引；
- [Programmer Edition](https://github.com/1c7/chinese-independent-developer/blob/master/pages/README-Programmer-Edition.md)：独立开发者项目；
- [2018–2020](https://github.com/1c7/chinese-independent-developer/blob/master/pages/README-2018-2020.md)：历史项目和长期验证信号；
- [Game](https://github.com/1c7/chinese-independent-developer/blob/master/pages/README-Game.md)：游戏、流量和游戏变现案例。

根据问题类型，Skill 还会查询 GitHub Trending、Awesome Selfhosted、HelloGitHub、Hugging Face、Papers With Code、Agent 和 LLM 应用集合、Libraries.io、LFX Insights、中国开源生态、Product Hunt 和独立开发者案例。完整来源见 [references/source-catalog.md](references/source-catalog.md)。

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
找 10 个可以在 30 天内改造成 B2B SaaS 的开源项目，并说明哪些可以直接商用。
```

```text
使用 $open-source-opportunity-loop。
把这些开源项目组合成一个适合中国制造业的 AI 产品，给出技术路线、客户和收费方式。
```

## 标准输出

每次推荐应包含：

1. 需求理解和关键假设；
2. 直接底座、模块、AI 能力和市场参考；
3. License、维护、部署和区域适配风险；
4. 推荐的项目组合；
5. 7 天 MVP；
6. 30 天产品版本；
7. 私有部署或服务路线；
8. 变现假设和下一步验证实验。

## 许可证与注意事项

本仓库使用 [MIT License](LICENSE)。但本 Skill 推荐的第三方项目、模型、数据集、字体、图片和商标都有各自的授权条件，不能因为被收录或被推荐就默认可以商用。

使用前必须回到原项目仓库核对 License 和 Notice。这个 Skill 提供的是实用研究建议，不构成法律、财务或合规意见。

Skill 不会要求用户在对话中粘贴 GitHub Token。需要 GitHub 权限时，请使用本机 `gh auth login` 或受保护的环境变量。

## 贡献与验证

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，并在提交前运行：

```bash
python3 scripts/validate_skill.py
```

## English

> Turn a product idea into an open-source-backed MVP and a practical commercialization plan.

## What it does

Open Source Opportunity Loop is a reusable Codex Skill for dialogue-first discovery and product planning. Give it a product idea in one sentence. It routes the idea through open-source project discovery, AI capability search, license and maintenance checks, market evidence, MVP planning, and monetization experiments.

It is designed to answer:

- What can I reuse or combine?
- Can I legally and practically adopt it?
- What should I build in 7 days?
- What should become a 30-day product?
- Should I sell SaaS, private deployment, a productized service, a plugin, or a template?

## Core loop

```text
Idea -> intent -> discovery -> verification -> composition -> market validation
     -> MVP and monetization plan -> feedback -> refined recommendation
```

## Included sources

The Skill starts with four baseline collections:

- [sindresorhus/awesome](https://github.com/sindresorhus/awesome)
- [Chinese Independent Developer — Programmer Edition](https://github.com/1c7/chinese-independent-developer/blob/master/pages/README-Programmer-Edition.md)
- [Chinese Independent Developer — 2018–2020](https://github.com/1c7/chinese-independent-developer/blob/master/pages/README-2018-2020.md)
- [Chinese Independent Developer — Game](https://github.com/1c7/chinese-independent-developer/blob/master/pages/README-Game.md)

It also routes to GitHub Trending, Awesome Selfhosted, HelloGitHub, Hugging Face, Papers With Code, agent and LLM app collections, Libraries.io, LFX Insights, Chinese open-source ecosystems, Product Hunt, and indie-founder sources. See [references/source-catalog.md](references/source-catalog.md).

## Use it

Install or copy this repository into the Skills directory used by your agent, then invoke it explicitly:

```text
$open-source-opportunity-loop
```

Example prompts:

```text
Use $open-source-opportunity-loop. I want to build an AI content system for Chinese ceramic exporters. Find reusable open-source bases, check licenses, and give me a 7-day MVP and monetization plan.

Use $open-source-opportunity-loop. Find ten open-source projects that can become a small B2B SaaS within 30 days.

Use $open-source-opportunity-loop. Compare these projects for license risk, maintenance, deployment effort, and commercial potential.
```

## Output

The Skill returns:

1. intent and assumptions;
2. candidate projects grouped as direct bases, modules, AI capabilities, and market references;
3. license, maintenance, deployment, and regional risks;
4. a recommended composition;
5. 7-day MVP, 30-day product, and private-deployment/service routes;
6. monetization hypotheses and the next validation experiment.

## Repository structure

```text
SKILL.md                         Core instructions
agents/openai.yaml               UI metadata and invocation prompt
references/                      Source, search, license, and monetization guidance
examples/                        Worked product scenarios
scripts/validate_skill.py        Dependency-free structure validation
.github/                         CI and contribution templates
```

## License and safety

This repository is licensed under the [MIT License](LICENSE). The Skill's license does not grant rights to third-party projects, models, datasets, fonts, images, or trademarks it references. Always verify the original project's license and notices before commercial use.

The Skill is practical research guidance, not legal, financial, or compliance advice. It must not request personal access tokens in chat. Use local GitHub authentication such as `gh auth login` or a protected environment variable.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Run the validator before submitting changes:

```bash
python3 scripts/validate_skill.py
```

## Documentation

- [中文 README](#简体中文)
- [Chinese full README](README.zh-CN.md)
- [Source catalog](references/source-catalog.md)
- [Search workflow](references/search-workflow.md)
- [License and project health](references/license-and-health.md)
- [Monetization playbook](references/monetization-playbook.md)
