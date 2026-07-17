# License and Project Health

This is practical product guidance, not legal advice. Always read the exact license and notices in the original repository before shipping.

## License triage

| Label | Typical interpretation | Action |
|---|---|---|
| Direct | A permissive license is clearly present and obligations are understood | May be considered for direct reuse after dependency review |
| Conditions | Copyleft, dual licensing, model restrictions, or unclear third-party assets exist | Isolate the component and get a legal review before distribution |
| Reference only | The project has no clear license, is a product listing, or only shows a demo | Use ideas and architecture; do not copy code |
| Avoid | License conflict, prohibited use, abandoned critical dependency, or material security concern | Do not recommend for the proposed commercial path |

## Checks

1. Open the repository's `LICENSE`, `COPYING`, or license metadata.
2. Check whether dependencies carry separate licenses.
3. Check model weights, datasets, fonts, images, and sample data separately.
4. Check trademark and brand-use notices.
5. Check whether the intended distribution is hosted SaaS, binary distribution, embedded library, or private deployment.
6. Record the verification date and link to the source.

## Health signals

Use multiple signals:

- recent meaningful commits or releases;
- more than one active contributor;
- issue and pull-request response patterns;
- release cadence and upgrade path;
- documentation and installation reproducibility;
- security advisories and dependency freshness;
- community or foundation governance.

Stars and forks are discovery signals, not maintenance proof.

## Output language

Use plain labels in the final answer:

- “可以直接作为底座，但仍需核对依赖许可证。”
- “适合参考架构，不建议直接复制代码。”
- “项目活跃度不足，不作为首选。”
- “许可证未明确，暂停商业化判断。”
