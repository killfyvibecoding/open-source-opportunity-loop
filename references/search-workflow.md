# Search Workflow

## Route before search

Search is not always the first step. First select the current route:

```text
vague idea -> positioning
product direction or value unclear -> product discovery
clear idea without candidates -> discovery
named repository -> adoption review
candidate list -> composition
clear product without evidence -> commercial validation
validated pilot -> MVP execution
previous result or “continue” -> continuation
```

Only search when the selected route needs fresh evidence. For a vague idea, clarify the paid workflow before collecting projects.

## Intent schema

Turn a natural-language request into this object before searching:

```yaml
industry: ""
customer: ""
buyer: ""
job_to_be_done: ""
pain: ""
desired_outcome: ""
opportunity: ""
success_metric: ""
product_form: "saas | private-deployment | app | plugin | service | game | content"
region: "china | overseas | both"
ai_role: "none | assistant | rag | workflow | agent | model | multimodal"
video_role: "none | capture | edit | generate | publish | analyze"
constraints:
  team: ""
  budget: ""
  deadline: ""
  hosting: ""
  language: ""
goal: "validate | ship-mvp | sell-service | build-business"
product_stage: "discovery | validation | MVP | growth"
```

If the user gives only an idea, infer the fields and label assumptions explicitly.

For an unclear idea, add:

```yaml
current_route: "positioning"
buyer: "unknown"
scenario: "unknown"
desired_outcome: "unknown"
evidence_gap: ""
next_question: ""
```

## Candidate record

Every recommended project should be normalized to:

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
product_fit: "high | medium | low"
validation_role: "prototype | experiment | MVP | production"
commercial_use: "direct | conditions | reference-only | avoid"
risks: []
evidence: []
```

Do not fill unknown fields with guesses.

## Recommendation score

Use the score as a decision aid, not as an objective truth:

```text
business fit        20
product fit         20
license clarity     20
maintenance         15
deployment effort   15
regional fit         5
monetization fit     5
```

Explain the two or three factors that drive the score. A high-star project with a weak license or no recent maintenance should not rank first.

## Route selection

Choose the route based on the user's goal:

- **Validate**: prioritize a narrow workflow, manual operations, and three target users.
- **Ship MVP**: prioritize a direct base, low deployment effort, and one measurable outcome.
- **Sell service**: prioritize private deployment, data control, customization, and support.
- **Build SaaS**: prioritize tenant isolation, billing, observability, upgrades, and license compatibility.
- **Build game or traffic product**: use the Game collection and current distribution evidence before selecting a technical base.
- **Positioning**: translate broad capabilities into a buyer, recurring scenario, and measurable business result before recommending architecture.
- **Product discovery**: define the desired outcome, customer job, opportunity, solution hypotheses, riskiest assumption, and experiment before searching for repositories.
- **Continue**: inspect the previous result and advance one state only; do not repeat completed research.

## Answer template

```markdown
## 结论

一句话给出推荐方向。

## 当前路由

说明本轮是在定位、发现、核验、组合、商业验证、MVP 执行还是续接。

## 需求理解

列出行业、用户、买方、客户任务、目标结果、机会点、产品形态和关键假设。

## 产品思考

如果本轮属于产品发现或定位，先输出 outcome -> opportunity -> solution -> experiment，并明确最大风险假设和成功阈值。

## 推荐项目

| 项目 | 角色 | 为什么匹配 | License/活跃度 | 商业化判断 |
|---|---|---|---|---|

## 组合方案

说明哪些项目组合在一起，以及数据如何流动。

## 三条路线

### 7 天 MVP
### 30 天产品
### 私有部署/服务

## 变现假设

区分已观察信号、推断和待验证实验。

## 风险

License、模型、数据、部署、获客和成本风险。

## 下一步

只给一个最重要的下一步。
```
