# State and Feedback

## Default behavior

Keep working state in the conversation. Do not create local files, databases, or external records unless the user asks or approves.

At the end of a substantial response, retain this compact state mentally or in the response:

```yaml
current_route: "positioning | discovery | adoption-review | composition | commercial-validation | mvp-execution | continuation"
problem_statement: ""
buyer: ""
selected_direction: ""
candidate_projects: []
verified_facts: []
assumptions: []
open_questions: []
next_action: ""
```

## Optional project record

If the user wants persistence, create or update a project record only after confirming the target path. Keep these sections separate:

```text
facts/       source-backed facts and links
assumptions/ hypotheses with confidence
decisions/   selected direction and rejected alternatives
experiments/ tests, dates, results, and follow-up
```

Facts must include a source. AI conclusions must be marked as conclusions. Experiment results must not be rewritten as original facts.

## Feedback handling

Interpret feedback as a state transition:

| Feedback | Next route |
|---|---|
| “客户不是这个人” | Positioning |
| “这个项目太重” | Discovery or Composition |
| “许可证不行” | Adoption review or replacement discovery |
| “我已经有客户” | MVP execution or Commercial validation |
| “我还不知道怎么收费” | Commercial validation |
| “这个方向可以” | MVP execution |
| “继续” | Continuation navigation |

Never treat a positive reaction as market validation. Convert it into a testable next action.

