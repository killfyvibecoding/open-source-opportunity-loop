# Product Thinking Layer

This reference adds a product-discovery layer to the Open Source Opportunity Loop. It is conceptually informed by the public methods in [phuryn/pm-skills](https://github.com/phuryn/pm-skills), including opportunity mapping, assumption prioritization, experiments, product strategy, and Lean Canvas. It does not copy that repository's Skill files, commands, wording, or assets.

## When to use it

Read this reference before technical discovery when the user asks:

- “我到底应该做什么产品？” / “What should I build?”
- “这个想法值不值得做？” / “Is this idea worth building?”
- “用户是谁、痛点是什么？” / “Who is the user and what is the pain?”
- “先帮我梳理产品思路。” / “Help me think through the product first.”
- “功能太多，MVP 怎么取舍？” / “How should I prioritize the MVP?”

Do not force the complete framework when the user has already named a validated workflow and only needs an implementation step.

## Product brief

Turn the user's natural language into a brief. Mark unknowns as assumptions instead of filling them with confidence.

```yaml
user: ""
buyer: ""
job_to_be_done: ""
current_alternative: ""
problem: ""
desired_outcome: ""
opportunity: ""
solution_hypotheses: []
riskiest_assumptions: []
success_metric: ""
success_threshold: ""
product_stage: "discovery | validation | MVP | growth"
```

The daily user and the paying buyer can be different. Keep both visible. A feature is not a problem statement; rewrite “需要一个 AI 图片生成器” as the job and outcome it is meant to improve.

## Outcome-to-experiment chain

Use one desired outcome at a time. Map the product decision as:

```text
desired outcome
  -> customer job / unmet need
  -> opportunity
  -> solution hypotheses
  -> riskiest assumption
  -> experiment
  -> evidence
```

### Outcome

Use a measurable change for a specific user or business, such as “reduce the time for a shop operator to publish one complete SKU from 30 minutes to 5 minutes.” Avoid “build an AI platform” as an outcome.

### Opportunity

Describe a customer need or obstacle from the customer's perspective:

- “我需要为同一 SKU 生成多个渠道规格，但每次都要重复改图和改文案。”
- “销售拿不到统一的产品资料，回复询盘时反复找 PDF。”

An opportunity is not a feature. Keep related needs together and prioritize the two or three that most affect the chosen outcome.

### Solution hypotheses

Generate at least three materially different solutions before choosing one. They can include a manual service, a lightweight workflow, a plugin, or a full product. Use open-source repositories only as implementation candidates for a solution hypothesis.

### Experiment

Prefer behavior over opinions. Each experiment must state:

```yaml
hypothesis: ""
method: "landing-page | concierge-service | clickable-demo | manual-batch | prototype | paid-pilot"
target_users: ""
behavior_observed: ""
metric: ""
success_threshold: ""
time_box: ""
decision: "continue | revise | stop"
```

“用户说喜欢” is a signal, not validation. Look for a completed task, uploaded data, repeat use, referral, meeting, deposit, or paid pilot.

## Assumption map

For an early idea, inspect the assumptions that could make the product fail:

| Risk area | Question |
|---|---|
| Value | Will the target user choose this over the current workaround? |
| Usability | Can the user complete the job with the available input and guidance? |
| Viability | Will the buyer pay enough to cover delivery and support? |
| Feasibility | Can the workflow meet the required quality, latency, and volume? |
| Go-to-market | Can the first users be reached through a realistic channel? |
| Strategy | Does this narrow workflow create a defendable or expandable position? |
| Team | Can this team access the users, data, skills, and operational capacity? |
| Compliance | Can the data, model, content, payment, and hosting arrangement be used in the target region? |

Prioritize an assumption when its failure would invalidate the direction and the uncertainty is high. Use a qualitative Impact × Risk matrix; do not present a score as objective market truth.

## MVP contract

An MVP is the smallest product or service that can test the riskiest assumption. Before recommending an MVP, require:

- one target user and one paying buyer, if they differ;
- one recurring job;
- one input and one useful output;
- a manual fallback for expensive or unreliable steps;
- one behavior-based success metric and threshold;
- a time box and a decision after the test.

For open-source-backed MVPs, separate the product test from the infrastructure test. Do not spend two weeks deploying a complete platform to answer whether three customers want one workflow.

## Opportunity Solution Tree, kept lightweight

Use this hierarchy when several directions compete:

```text
Outcome
├── Opportunity A
│   ├── Solution A1 -> Experiment A1
│   └── Solution A2 -> Experiment A2
└── Opportunity B
    ├── Solution B1 -> Experiment B1
    └── Solution B2 -> Experiment B2
```

Keep one outcome per tree. If an experiment fails, revise or kill the solution branch; do not quietly redefine success.

## Lean Canvas use

Use a Lean Canvas only when the user needs business-model clarity or commercialization. Keep it hypothesis-driven:

1. Problem
2. Customer segments and early adopters
3. Unique value proposition
4. Solution
5. Channels
6. Revenue streams
7. Cost structure
8. Key metrics
9. Unfair advantage or current defensibility hypothesis

Do not fill every box with invented market numbers. Label evidence, inference, and experiment separately.

## Choosing the next route

| Evidence state | Next route |
|---|---|
| Buyer, job, and outcome unclear | Positioning |
| Job is clear but opportunity or value is uncertain | Product discovery experiment |
| Opportunity is clear but no implementation candidate exists | Discovery |
| Candidate exists but adoption risk is unclear | Adoption review |
| Candidate and product brief fit | Composition or MVP execution |
| Users complete the job but payment is uncertain | Commercial validation |
| Pilot or paid usage repeats | 30-day product or private deployment |

Return one decision and one next action. Mention later stages only as context.

## Product-thinking output contract

When this layer is active, include:

```markdown
## 产品思考 / Product thinking
- 用户 / Buyer:
- 客户任务 / Job to be done:
- 当前替代方案 / Current alternative:
- 目标结果 / Desired outcome:
- 机会点 / Opportunity:
- 解决方案假设 / Solution hypotheses:
- 最大风险假设 / Riskiest assumption:
- 本轮实验 / Next experiment:
- 成功阈值 / Success threshold:
```

Then connect the chosen solution hypothesis to open-source candidates. Do not let the candidate list replace this section.
