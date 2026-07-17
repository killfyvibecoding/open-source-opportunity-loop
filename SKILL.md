---
name: open-source-opportunity-loop
description: "Turn a vague product idea into a focused business opportunity, an open-source-backed MVP, and a practical commercialization path. Use when the user wants to discover reusable projects, evaluate technical or license fit, combine open-source components, clarify a product direction, or decide the next step after a previous analysis."
---

# Open Source Opportunity Loop

## Role

This is a single-entry, dialogue-first decision Skill. The user can describe what they want to do in natural language. The Skill identifies the current task, clarifies the business problem when needed, routes to the smallest useful research path, verifies open-source adoption risk, and returns one practical next step.

It is not a directory dump, a fixed checklist, or a promise that every listed project can be commercialized.

## Operating principles

- Start from the user's current intent, not from a preselected tool or source.
- Use one route and one next action per response. Do not force a fixed chain such as A -> B -> C.
- Ask at most one question when the missing answer would change the route materially.
- Separate evidence, inference, recommendation, and experiment.
- Verify the original repository, license, dependencies, and maintenance before recommending direct reuse.
- Prefer a narrow paid workflow over a broad platform when the idea is still vague.
- Keep state in the conversation by default. Only write project notes or decision records when the user asks or approves it.
- Never copy code, text, assets, or knowledge bases from third-party Skills without checking their license and attribution requirements.

## Single-entry router

Inspect the current conversation before answering. Reuse existing candidates, assumptions, decisions, and user feedback instead of restarting research.

Select exactly one mode:

| Mode | Trigger | First output |
|---|---|---|
| Onboarding | The user asks how to use the Skill or gives no concrete task | Explain the available outcomes and ask for the user's real idea |
| Positioning | The idea is broad, ambiguous, or combines several capabilities | Produce up to three business problem framings and recommend one |
| Discovery | The user asks what open-source projects can be reused | Search and rank candidates by role |
| Adoption review | The user asks whether a named project can be used or commercialized | Check license, health, deployment, dependencies, and restrictions |
| Composition | The user has candidates and wants a product architecture | Combine only the smallest coherent set of components |
| Commercial validation | The user asks who pays, how to charge, or whether it is worth building | Define buyer, paid job, evidence, and the next experiment |
| MVP execution | The direction is clear and the user wants to build | Produce a time-boxed MVP scope and implementation order |
| Continuation | The previous response produced a result and the user says continue, revises it, or gives feedback | Choose the single most valuable next route |
| Decision record | The user asks to save, compare, or revisit a decision | Record facts, assumptions, decisions, and open questions with clear labels |

Announce the selected route in one sentence when useful, for example: “这个问题先进入定位澄清，我先把 AI 和视频拆成可收费的业务切口。” Then execute that route.

## Main operating sequence

### Phase 0: Read the current state

Before research, identify:

- what the user explicitly wants now;
- what has already been concluded in this conversation;
- which candidate projects or sources have already been reviewed;
- whether the user is asking for a new direction, a decision, an implementation step, or a follow-up;
- whether current information needs web verification.

Do not repeat a completed search merely because the user asks to continue.

### Phase 1: Normalize the problem

Convert the request into this working brief and label assumptions:

```yaml
industry: ""
customer: ""
buyer: ""
scenario: ""
pain: ""
desired_outcome: ""
product_form: "saas | private-deployment | app | plugin | service | game | content | index"
region: "china | overseas | both"
ai_role: "none | assistant | rag | workflow | agent | model | multimodal"
video_role: "none | capture | edit | generate | publish | analyze"
constraints:
  team: ""
  budget: ""
  deadline: ""
  hosting: ""
  language: ""
  compliance: ""
goal: "validate | ship-mvp | sell-service | build-business"
```

If the idea is vague, do not begin with a large project list. First create up to three positionings using:

```text
target buyer + high-frequency scenario + measurable result + delivery form
```

Rank the positionings by urgency, ability to pay, data availability, delivery difficulty, and speed of validation. State which facts are unknown. Ask one focused question only if a choice is necessary to continue.

### Phase 2: Select the research route

Route only to the smallest useful source set:

- **Reuse discovery**: the four baseline collections, GitHub, Awesome Selfhosted, HelloGitHub, OpenResource, Open Source Atlas, and Gitee.
- **AI and video capability**: Hugging Face, Papers With Code, official model repositories, `awesome-agents`, `awesome-llm-apps`, FFmpeg, video workflow projects, and relevant official documentation.
- **Technical adoption**: the original repository, releases, commits, issues, pull requests, dependency files, Libraries.io, and LFX Insights when available.
- **Market and distribution**: Product Hunt, Indie Hackers, IndieTools, Chinese industry cases, WeChat or enterprise WeChat workflows, short-video platforms, and relevant current market evidence.
- **Continuation**: current conversation, prior candidate records, saved notes, and unresolved questions. Do not search again unless the next route requires fresh evidence.

The four baseline knowledge collections remain the foundation:

- `sindresorhus/awesome` for broad technical indexes;
- `README-Programmer-Edition.md` for independent developer products;
- `README-2018-2020.md` for historical projects and survival signals;
- `README-Game.md` for games, traffic loops, and attention monetization.

Use [references/source-catalog.md](references/source-catalog.md) for canonical links and source roles.

### Phase 3: Discover and compare candidates

When discovery is the selected route, return 5–12 candidates grouped by role:

1. **Direct base** — the closest reusable application or framework.
2. **Composable module** — one capability such as authentication, workflow, CRM, video processing, search, or billing.
3. **AI capability** — model, dataset, RAG, agent, evaluation, or multimodal component.
4. **Market reference** — an existing product or business pattern, not necessarily open source.

Normalize each candidate as:

```yaml
name: ""
official_url: ""
repository_url: ""
role: "direct-base | module | ai-capability | market-reference"
what_it_does: ""
license: "unknown"
maintenance_signal: "unknown"
deployment: "unknown"
fit: "high | medium | low"
commercial_use: "direct | conditions | reference-only | avoid"
risks: []
evidence: []
```

Use this score only as a decision aid:

```text
business fit        30
license clarity     20
maintenance         15
deployment effort   15
regional fit        10
monetization fit    10
```

Explain the two or three factors that drive the ranking. A high-star project with a weak license or no meaningful maintenance should not rank first.

### Phase 4: Pass the adoption gate

Before recommending direct reuse, verify:

- exact license and root-level notices;
- whether commercial use, redistribution, SaaS use, or model use has conditions;
- last meaningful commit or release, contributors, issue and pull-request activity;
- database, storage, model/API, GPU, and deployment requirements;
- third-party assets, model weights, datasets, fonts, trademarks, and API terms;
- China-specific hosting, data-residency, payment, API availability, and compliance concerns when relevant.

Classify every project as **direct reuse**, **reuse with conditions**, **reference only**, or **avoid**. Use [references/license-and-health.md](references/license-and-health.md). State that this is practical guidance, not legal advice.

### Phase 5: Pass the commercial gate

For the recommended direction, identify:

- the paying buyer and the daily user;
- the expensive or frequent job being solved;
- the buyer's current workaround;
- the event that creates willingness to pay;
- the acquisition channel;
- delivery, API, hosting, and support costs;
- the smallest paid pilot that can be delivered manually.

Label every important statement as one of:

- **Evidence**: an observed project, customer statement, published case, repository signal, or current source;
- **Inference**: a reasoned hypothesis based on evidence;
- **Experiment**: a test required before building more.

Use [references/monetization-playbook.md](references/monetization-playbook.md) for SaaS, open-core, private deployment, productized service, template, plugin, API, and content-led models.

### Phase 6: Choose one delivery route

For a product idea, compare these routes internally, but recommend only one current route:

| Route | Use when | Minimum output |
|---|---|---|
| 7-day MVP | The problem or buyer still needs validation | one workflow, manual fallback, three test users, one success metric |
| 30-day product | The workflow has evidence and repeats | product architecture, auth, data, billing, deployment, metrics |
| Private deployment/service | Data control, customization, or trust matters | delivery scope, price hypothesis, installation, support boundary |
| Content/traffic product | Distribution is the main advantage | content unit, publishing loop, conversion event, retention metric |
| Index/retrieval site | Discovery and comparison are the product | source ingestion, normalized records, filters, evidence links, lead capture |

Prefer the smallest route that can create a paid or behavior-based signal.

### Phase 7: Return an actionable artifact

Use the user's language and return:

```markdown
## 结论 / Recommendation
## 当前路由 / Current route
## 需求理解与假设 / Intent and assumptions
## 推荐项目 / Candidate projects
## 技术与许可证闸门 / Adoption gate
## 商业验证 / Commercial validation
## 推荐方案 / Recommended route
## MVP 交付物 / MVP artifact
## 风险 / Risks
## 下一步 / One next action
```

For a vague idea, the artifact should be a positioning brief before it is an architecture. For a named repository, the artifact should be an adoption review before it is a build plan. For a clear validated direction, the artifact should be an MVP execution plan.

### Phase 8: Continue through feedback

End with one small decision request, such as:

- “你更倾向 SaaS、私有部署，还是先做服务？”
- “保留这三个项目，还是换成更轻量的底座？”
- “你愿意先找三个真实客户做访谈吗？”

Use the answer to select the next route. Examples:

- no clear buyer -> commercial validation;
- no clear pain -> positioning;
- no suitable technical base -> discovery;
- license or deployment risk -> adoption review;
- clear pilot customer -> MVP execution;
- too many alternatives -> decision record;
- user says “继续” -> post-task navigation from the last result.

Do not restart the full loop unless the target problem changed.

### Phase 9: Optional state and decision records

Conversation state is the default. If the user asks to save or revisit the work, maintain a lightweight project record using [references/state-and-feedback.md](references/state-and-feedback.md):

- facts and source links;
- assumptions and confidence;
- selected direction;
- rejected alternatives and why;
- open questions;
- experiment results;
- next route.

Do not silently create or modify local files, databases, or external services.

## Quality and safety rules

- Prefer a small coherent project combination over a long list.
- Never imply that inclusion in a collection makes a project commercially usable.
- Never invent current stars, releases, prices, or maintenance status; browse and cite current sources when needed.
- Treat historical projects as learning and survival signals, not proof of current activity.
- Treat market directories as references, not open-source repositories.
- Include China-specific concerns when relevant: domestic model availability, WeChat or enterprise WeChat, ICP/data compliance, private deployment, local payment, and overseas API dependency.
- If API credentials are needed, instruct the user to use `gh auth login` or a protected local environment variable. Never ask for a personal access token in chat.
- Do not copy third-party Skill code, text, assets, or knowledge bases without permission and license compatibility.

## Reference files

- [Source catalog](references/source-catalog.md)
- [Interaction router](references/interaction-router.md)
- [Search workflow](references/search-workflow.md)
- [License and health](references/license-and-health.md)
- [Monetization playbook](references/monetization-playbook.md)
- [State and feedback](references/state-and-feedback.md)
- [Inspiration and license boundaries](references/inspiration-and-boundaries.md)

## Worked examples

- [Ceramic export AI](examples/ceramic-export-ai.md)
- [Content production system](examples/content-production.md)
- [Game and traffic loop](examples/game-and-traffic.md)
- [Continuation loop](examples/continuation-loop.md)
