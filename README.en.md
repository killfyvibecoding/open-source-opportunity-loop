# Open Source Opportunity Loop 🔁

[![GitHub stars](https://img.shields.io/github/stars/killfyvibecoding/open-source-opportunity-loop?style=flat-square)](https://github.com/killfyvibecoding/open-source-opportunity-loop/stargazers)
[![Issues](https://img.shields.io/github/issues/killfyvibecoding/open-source-opportunity-loop?style=flat-square)](https://github.com/killfyvibecoding/open-source-opportunity-loop/issues)
[![Forks](https://img.shields.io/github/forks/killfyvibecoding/open-source-opportunity-loop?style=flat-square)](https://github.com/killfyvibecoding/open-source-opportunity-loop/network/members)
[![License](https://img.shields.io/github/license/killfyvibecoding/open-source-opportunity-loop?style=flat-square)](LICENSE)
[![Validate Skill](https://github.com/killfyvibecoding/open-source-opportunity-loop/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/killfyvibecoding/open-source-opportunity-loop/actions/workflows/validate-skill.yml)

### [简体中文](README.md) | English

> Turn a product idea into reusable open-source foundations, a testable MVP, and a practical commercialization path.

## ⚠️ Important note

This project is a reusable **Codex Skill**, not a ready-to-run website or SaaS application.

It runs inside a Skill-capable AI Agent and supports:

- open-source project discovery;
- matching AI models, datasets, RAG, and agent workflows;
- license, maintenance, deployment, and dependency checks;
- MVP, private-deployment, and SaaS route design;
- market validation and monetization planning.

Third-party projects, models, datasets, fonts, images, and trademarks have their own terms. Being listed or recommended does not mean that an artifact is commercially reusable. Always verify the original repository's license and notices.

## The decision loop

```text
User idea
  ↓
Intent extraction
  ↓
Open-source discovery
  ↓
Technical, license, and maintenance verification
  ↓
Solution composition
  ↓
Market and monetization validation
  ↓
7-day MVP / 30-day product / private-deployment plan
  ↓
User feedback and refined recommendation
```

## Three-layer framework

### 1. Project discovery

Answers: “What can I reuse or combine?”

- GitHub Trending;
- Awesome Selfhosted;
- HelloGitHub;
- OpenResource, Open Source Atlas, and Gitee;
- `sindresorhus/awesome`;
- Chinese Independent Developer collections: Programmer Edition, 2018–2020, and Game.

### 2. Technical verification

Answers: “Can I adopt, deploy, and commercialize it?”

- Hugging Face;
- Papers With Code;
- `awesome-agents` and `awesome-llm-apps`;
- Libraries.io;
- LFX Insights;
- Alibaba Open Source, ByteDance Open Source, Apache, and Eclipse.

### 3. Market and monetization

Answers: “Who pays, how do they pay, and what should I validate first?”

- Indie Hacker Projects;
- Indie Hacker Stacks;
- Product Hunt;
- Indie Hackers;
- IndieTools;
- Open Source Alternative.

See [references/source-catalog.md](references/source-catalog.md) for the full source map.

## Use it

Clone the repository into the Skills directory used by your Agent and invoke:

```text
$open-source-opportunity-loop
```

Example:

```text
Use $open-source-opportunity-loop.
I want to build an AI content system for Chinese ceramic exporters. Find reusable open-source bases, check licenses, and give me a 7-day MVP and monetization plan.
```

## Standard output

The Skill returns:

1. intent and assumptions;
2. direct bases, modules, AI capabilities, and market references;
3. license, maintenance, deployment, and regional risks;
4. a recommended composition;
5. a 7-day MVP;
6. a 30-day product route;
7. a private-deployment or service route;
8. monetization hypotheses and the next validation experiment.

## Quick start

```bash
git clone https://github.com/killfyvibecoding/open-source-opportunity-loop.git
cd open-source-opportunity-loop
python3 scripts/validate_skill.py
```

Copy the directory into your Agent's Skills directory and invoke it with `$open-source-opportunity-loop`.

## Repository structure

```text
SKILL.md                         Core Skill workflow
agents/openai.yaml               Skill UI metadata and invocation prompt
references/                      Source, search, license, and monetization guidance
examples/                        Worked product scenarios
scripts/validate_skill.py        Dependency-free structure validation
.github/                         CI, issue, and pull-request templates
README.md                        Chinese project documentation
README.en.md                     English project documentation
README.zh-CN.md                  Extended Chinese documentation
```

## License

This repository is licensed under the [MIT License](LICENSE). The license does not cover third-party projects, models, datasets, fonts, images, or trademarks referenced by the Skill.

This Skill provides practical research guidance, not legal, financial, or compliance advice.

## Contributing and feedback

- Contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md)
- Security policy: [SECURITY.md](SECURITY.md)
- Issues: [GitHub Issues](https://github.com/killfyvibecoding/open-source-opportunity-loop/issues)
- Pull requests: [GitHub Pull Requests](https://github.com/killfyvibecoding/open-source-opportunity-loop/pulls)

## Documentation

- [Chinese documentation](README.md)
- [Extended Chinese documentation](README.zh-CN.md)
- [Source catalog](references/source-catalog.md)
- [Search workflow](references/search-workflow.md)
- [License and project health](references/license-and-health.md)
- [Monetization playbook](references/monetization-playbook.md)
