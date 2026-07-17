# Interaction Router

## Purpose

The Skill has one user-facing entry point. It decides what to do from the user's current sentence and the conversation state. The user does not need to select an internal module.

## Route priority

Evaluate routes in this order:

1. Explicit current request;
2. unfinished result or user feedback from the previous turn;
3. clarity of the business problem;
4. need for fresh technical or market evidence;
5. optional recording request.

Use the first route that resolves the user's current bottleneck.

## Route table

| Current signal | Route | Deliverable |
|---|---|---|
| “我想做一个……” but buyer or job is unclear | Positioning | three problem framings, one recommendation, one question |
| “找开源项目/底座” | Discovery | ranked candidates with role and evidence |
| “这个项目能不能用/商用” | Adoption review | license, maintenance, deployment, and risk classification |
| “把这些项目组合起来” | Composition | minimal architecture and data flow |
| “有没有市场/怎么赚钱” | Commercial validation | buyer, paid job, pricing hypothesis, acquisition test |
| “先做 MVP/怎么开发” | MVP execution | time-boxed scope, reused components, acceptance metric |
| “继续/根据上面优化” | Continuation | one next route based on the prior result |
| “保存/记录/以后继续” | Decision record | facts, assumptions, decision, open questions, next route |

## Positioning route

When a request mixes technologies such as AI, video, and a broad industry, first translate capabilities into a paid workflow. Use this structure:

```text
buyer + high-frequency scenario + input + AI/video action + measurable business result
```

Do not define the product as “an AI and video platform” until the customer, workflow, and outcome are clear.

## Continuation route

Read the previous answer and classify its stopping point:

- unresolved customer or pain -> positioning or commercial validation;
- candidate list without verification -> adoption review;
- verified candidates without a product shape -> composition;
- product shape without evidence -> MVP validation;
- clear pilot or user -> MVP execution;
- completed experiment -> decision record and next experiment.

The next response should advance one state only. It may mention later states, but it should not execute all of them at once.

## Output contract

Every routed response should make four things visible:

1. current route;
2. conclusion or artifact produced now;
3. uncertainty or evidence gap;
4. one next action or one focused question.

