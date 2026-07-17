# Open Source Opportunity Loop

> Turn a product idea into an open-source-backed MVP and a practical commercialization plan.

[中文说明](README.zh-CN.md)

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

- [中文 README](README.zh-CN.md)
- [Source catalog](references/source-catalog.md)
- [Search workflow](references/search-workflow.md)
- [License and project health](references/license-and-health.md)
- [Monetization playbook](references/monetization-playbook.md)
