# Open Source Opportunity Loop 🔁

[![GitHub stars](https://img.shields.io/github/stars/killfyvibecoding/open-source-opportunity-loop?style=flat-square)](https://github.com/killfyvibecoding/open-source-opportunity-loop/stargazers)
[![Issues](https://img.shields.io/github/issues/killfyvibecoding/open-source-opportunity-loop?style=flat-square)](https://github.com/killfyvibecoding/open-source-opportunity-loop/issues)
[![Forks](https://img.shields.io/github/forks/killfyvibecoding/open-source-opportunity-loop?style=flat-square)](https://github.com/killfyvibecoding/open-source-opportunity-loop/network/members)
[![License](https://img.shields.io/github/license/killfyvibecoding/open-source-opportunity-loop?style=flat-square)](LICENSE)
[![Validate Skill](https://github.com/killfyvibecoding/open-source-opportunity-loop/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/killfyvibecoding/open-source-opportunity-loop/actions/workflows/validate-skill.yml)

### 简体中文 | [English](README.en.md)

> 告诉我想做什么，自动澄清业务切口、找到开源底座、验证风险，并给出下一步 MVP 路线。

## ⚠️ 重要说明

本项目是一个可复用的 **Codex Skill**，不是开箱即用的网站或 SaaS 软件。

它需要运行在支持 Skill 的 AI Agent 环境中，并通过对话完成：

- 开源项目检索；
- AI 模型、数据集、RAG 和 Agent 方案匹配；
- License、活跃度、部署难度和第三方依赖核验；
- MVP、私有部署和 SaaS 路线设计；
- 市场验证与变现方案生成。

Skill 推荐的第三方项目、模型、数据集、字体、图片和商标都有各自的授权条件。被收录或被推荐不等于可以直接商用，请务必回到原项目仓库核对 License 和 Notice。

## 核心 Loop

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
MVP / 私有部署 / 服务路线
  ↓
一个可执行产物
  ↓
用户反馈 → 动态选择下一步
```

## 一个入口，动态选择下一步

用户不需要记住内部模块，直接说自然语言即可：

```text
我想给建材厂做一个 AI 和视频系统，但方向很模糊。
```

Skill 会先进入“定位澄清”，而不是马上罗列开源项目。之后会根据结果自动切换到项目发现、License 核验、技术组合、商业验证、7 天 MVP、私有部署或决策记录。每轮只推进一个最重要的状态；用户可以直接说“继续”，从上一次结果接着推进。

## 四层决策框架

### 1. 项目发现层

回答“有什么可以复用或组合”：

- GitHub Trending；
- Awesome Selfhosted；
- HelloGitHub；
- OpenResource、Open Source Atlas、Gitee；
- `sindresorhus/awesome`；
- 中国独立开发者 Programmer Edition、2018–2020 和 Game。

### 2. 技术核验层

回答“能不能用、能不能部署、能不能商用”：

- Hugging Face；
- Papers With Code；
- `awesome-agents`、`awesome-llm-apps`；
- Libraries.io；
- LFX Insights；
- 阿里开源、字节跳动开源、Apache、Eclipse。

### 3. 市场变现层

回答“谁会付费、怎么收费、先验证什么”：

- Indie Hacker Projects；
- Indie Hacker Stacks；
- Product Hunt；
- Indie Hackers；
- IndieTools；
- Open Source Alternative。

完整来源和用途见 [references/source-catalog.md](references/source-catalog.md)。

## 4. 产品思考层

本 Skill 已融合 [phuryn/pm-skills](https://github.com/phuryn/pm-skills) 的产品发现思路，但保留为一个更适合“开源项目 → MVP → 变现”的轻量层：

```text
目标结果 → 客户任务与机会点 → 解决方案假设 → 最大风险假设 → 最小验证实验 → 开源底座与 MVP
```

它会帮助你先回答“为谁解决什么问题”，再决定“用哪个开源项目实现”。支持机会树、假设优先级、实验设计、MVP 边界和 Lean Canvas；不会要求每次都填完整套产品文档。

## 使用方式

将仓库复制到你的 Agent 使用的 Skills 目录，然后调用：

```text
$open-source-opportunity-loop
```

### 示例一：制造业 AI 产品

```text
使用 $open-source-opportunity-loop。
我想做一个面向中国陶瓷外贸企业的 AI 内容系统，帮我找开源底座，检查 License，给出 7 天 MVP 和变现方案。
```

### 示例二：先定位模糊想法

```text
使用 $open-source-opportunity-loop。
我想给建材厂做一个 AI 和视频系统，但方向很模糊，先帮我清晰定位。
```

### 示例三：寻找可商业化项目

```text
使用 $open-source-opportunity-loop。
找 10 个可以在 30 天内改造成 B2B SaaS 的开源项目，并说明哪些可以直接商用。
```

### 示例四：组合多个项目

```text
使用 $open-source-opportunity-loop。
把这些开源项目组合成一个适合中国制造业的 AI 产品，给出技术路线、客户和收费方式。
```

## 标准输出

每次推荐应包含：

1. 当前路由、需求理解和关键假设；
2. 产品思考：用户、买方、客户任务、目标结果、机会点和最大风险假设；
3. 证据缺口和必要问题；
4. 直接底座、模块、AI 能力和市场参考；
5. License、维护、部署和区域适配风险；
6. 一个推荐路线及对应产物；
7. 一个最重要的下一步验证实验。

只有当用户进入相应阶段时，才展开 7 天 MVP、30 天产品或私有部署路线。

## 快速开始

```bash
git clone https://github.com/killfyvibecoding/open-source-opportunity-loop.git
cd open-source-opportunity-loop
python3 scripts/validate_skill.py
```

将本目录复制到 Agent 的 Skills 目录后，通过 `$open-source-opportunity-loop` 调用。

## 项目结构

```text
SKILL.md                         Skill 核心流程
agents/openai.yaml               Skill 展示和调用信息
references/                      来源、搜索、许可证和变现规则
references/product-thinking.md   产品发现、假设、实验和 MVP 方法
examples/                        陶瓷外贸、内容生产、游戏流量、续接 Loop 示例
scripts/validate_skill.py        无第三方依赖的结构验证脚本
.github/                         CI、Issue 和 PR 模板
README.md                        中文项目说明
README.en.md                     English documentation
README.zh-CN.md                  完整中文文档
```

## 许可证

本仓库使用 [MIT License](LICENSE)。但本 Skill 推荐的第三方项目、模型、数据集、字体、图片和商标不受本仓库许可证覆盖。

这个 Skill 提供的是实用研究建议，不构成法律、财务或合规意见。

## 贡献与反馈

- 贡献指南：[CONTRIBUTING.md](CONTRIBUTING.md)
- 安全问题：[SECURITY.md](SECURITY.md)
- 提交 Issue：[Issues](https://github.com/killfyvibecoding/open-source-opportunity-loop/issues)
- 提交 Pull Request：[Pull requests](https://github.com/killfyvibecoding/open-source-opportunity-loop/pulls)

## 相关文档

- [完整中文文档](README.zh-CN.md)
- [英文文档](README.en.md)
- [来源目录](references/source-catalog.md)
- [动态路由](references/interaction-router.md)
- [产品思考](references/product-thinking.md)
- [搜索流程](references/search-workflow.md)
- [许可证与项目健康度](references/license-and-health.md)
- [变现手册](references/monetization-playbook.md)
- [状态与反馈](references/state-and-feedback.md)
- [启发与授权边界](references/inspiration-and-boundaries.md)
