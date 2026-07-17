---
name: open-source-opportunity-loop
description: "Turn a product idea into an open-source-backed MVP and commercialization plan. Use when the user asks what to build, wants reusable open-source projects, needs AI models or agents, asks whether a project can be commercialized, or wants a concrete technical and monetization route from an idea."
---

# Open Source Opportunity Loop

## Purpose

Use this skill as a dialogue-first research and decision workflow. The user should be able to describe an idea in one sentence; the response should connect that idea to reusable open-source projects, technical feasibility, licensing and maintenance risk, market evidence, an MVP path, and a monetization plan.

This is not a directory dump. Make a recommendation and explain what to build first.

## Core Loop

Run the following loop for every substantive request:

```text
User idea
  -> intent extraction
  -> source routing
  -> candidate discovery
  -> license and health verification
  -> solution composition
  -> market and monetization validation
  -> MVP plan and next action
  -> user feedback
  -> refine the next recommendation
```

Treat the four user-provided collections as the baseline knowledge layer:

- `sindresorhus/awesome`: broad technology and project index.
- `README-Programmer-Edition.md`: independent developer products and ideas.
- `README-2018-2020.md`: historical projects and long-term validation signals.
- `README-Game.md`: game projects, traffic loops, and game monetization patterns.

Load the source map in [references/source-catalog.md](references/source-catalog.md) when choosing additional sources.

## Workflow

### 1. Extract the user's intent

Convert the user's sentence into a compact working brief. Infer missing fields when safe; ask one focused question only when the missing field changes the recommendation materially.

Capture:

```text
industry: target industry or audience
customer: buyer and end user
pain: job to be done
product_form: SaaS, private deployment, plugin, app, content product, game, or service
region: China, overseas, or both
ai_role: none, assistant, RAG, workflow, agent, model, or multimodal
constraints: budget, team size, deadline, hosting, language, compliance
goal: validate demand, ship MVP, sell services, or build a product business
```

### 2. Route sources by question

Do not query every source equally. Route the request to the smallest useful set:

- **What can I reuse?** GitHub Trending, Awesome Selfhosted, HelloGitHub, OpenResource, Open Source Atlas, Gitee, and the four baseline collections.
- **What can I build with AI?** Hugging Face, Papers With Code, `awesome-agents`, `awesome-llm-apps`, Alibaba Open Source, ByteDance Open Source.
- **Can I safely adopt it?** The original repository, its license, release history, issue activity, Libraries.io, and LFX Insights when available.
- **Will people pay?** Indie Hacker Projects, Indie Hacker Stacks, Product Hunt, Indie Hackers, IndieTools, and relevant Chinese-market evidence.
- **What survived over time?** `README-2018-2020`, repository history, releases, contributors, and current documentation.

Use [references/source-catalog.md](references/source-catalog.md) for canonical links and source roles.

### 3. Discover candidates

Return 5–12 candidates, grouped by role rather than by popularity:

1. **Direct base** — closest reusable application or framework.
2. **Composable modules** — pieces that solve a specific capability.
3. **AI capability** — model, dataset, RAG, agent, or evaluation layer.
4. **Market reference** — an existing product or business model, not necessarily open source.

For each candidate, record the official URL, repository URL, purpose, language, deployment model, and why it matches the user's problem. Do not present a project as reusable code if only a product page was found.

### 4. Verify technical and legal fit

Before recommending direct reuse, verify the original project. Record:

- exact license and whether it is present at the repository root;
- last meaningful commit or release, not only star count;
- contributors, issue and pull-request activity when visible;
- deployment path, database, model/API dependencies, and operational complexity;
- Chinese-language, domestic-cloud, and data-residency constraints when relevant;
- third-party assets, model weights, fonts, datasets, and trademark restrictions.

Classify each project as **direct reuse**, **reuse with conditions**, **reference only**, or **avoid**. Use [references/license-and-health.md](references/license-and-health.md). State that the assessment is practical guidance, not legal advice.

### 5. Compose three solution routes

Always produce up to three routes when the request is a product idea:

| Route | Purpose | Required output |
|---|---|---|
| 7-day MVP | Validate the smallest valuable workflow | features, reused projects, manual steps, test users |
| 30-day product | Turn the workflow into a repeatable product | architecture, auth, data, billing, deployment, metrics |
| Service/private deployment | Sell implementation before scale | buyer, delivery scope, pricing hypothesis, support model |

Prefer one recommended route. Explain why it is the best next step for the user's constraints.

### 6. Validate the business path

Use market sources to identify the buyer, urgent job, competing products, pricing shape, acquisition channel, and likely gross-cost drivers. Distinguish:

- **validated signal**: an observed product, user complaint, published revenue story, or active project;
- **inference**: a reasoned hypothesis based on several signals;
- **experiment**: the next test needed before building more.

Use [references/monetization-playbook.md](references/monetization-playbook.md) for open-core, SaaS, private deployment, productized service, template, plugin, API, and content-led models.

### 7. Return an actionable answer

Use the user's language. Keep the first answer decision-oriented and include:

```text
结论 / Recommendation
需求理解 / Intent
推荐项目 / Candidate projects
技术组合 / Composition
License 与维护风险 / Risks
7 天 MVP
30 天版本
私有部署或服务路线
变现假设
下一步验证
```

Link to official sources close to each claim. Never imply that inclusion in an awesome list makes a project commercially usable. Never invent current stars, releases, prices, or maintenance status; browse and cite them when the user asks for current information.

### 8. Close the feedback loop

End with a small decision request, not a long questionnaire. Examples:

- “你更倾向 SaaS、私有部署，还是先做服务？”
- “保留项目 1、3、5，还是换成更轻量的方案？”
- “你愿意先找 3 个真实客户做访谈吗？”

Use the user's selection to narrow the next response. Do not restart the entire research from scratch unless the target problem changed.

## Output quality rules

- Prefer a small, coherent project combination over a long list.
- Separate source evidence, inference, and recommendation.
- Verify licenses at the original repository before discussing commercial reuse.
- Treat historical projects as learning and survival signals, not proof of current activity.
- Treat Product Hunt and indie-founder sites as market references, not open-source repositories.
- Include China-specific concerns when relevant: domestic model availability, WeChat or enterprise WeChat, ICP/data compliance, private deployment, local payment, and overseas API dependency.
- When API credentials are needed, instruct the user to use `gh auth login` or a local environment variable. Never ask the user to paste a personal access token into chat.

## Reference files

- [Source catalog](references/source-catalog.md): baseline and additional source map.
- [Search workflow](references/search-workflow.md): fields, scoring, and response routing.
- [License and health](references/license-and-health.md): practical adoption checks.
- [Monetization playbook](references/monetization-playbook.md): business models and experiments.

## Worked examples

- [Ceramic export AI](examples/ceramic-export-ai.md)
- [Content production system](examples/content-production.md)
- [Game and traffic loop](examples/game-and-traffic.md)
