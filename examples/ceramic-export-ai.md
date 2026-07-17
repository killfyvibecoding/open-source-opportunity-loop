# Example: Ceramic Export AI Content System

## User request

> I want to build an AI content and inquiry system for Chinese ceramic manufacturers selling overseas.

## Intent extraction

```yaml
industry: ceramics and manufacturing
customer: export factories and trading companies
pain: product material is scattered; multilingual pages and inquiry replies are slow
product_form: saas or private deployment
region: both
ai_role: rag, workflow, translation, and assistant
goal: ship-mvp and sell-service
```

## Search route

1. Use the baseline Programmer Edition and `awesome` collection for product patterns.
2. Search Awesome Selfhosted and GitHub for knowledge bases, workflow tools, CRM, file parsing, and admin systems.
3. Search Hugging Face and `awesome-llm-apps` for multilingual RAG and document-processing examples.
4. Verify licenses and deployment before recommending a base.
5. Search Indie Hacker Projects and Indie Hackers for pricing and distribution patterns.

## Recommended output shape

```text
7-day MVP: upload product files -> extract facts -> generate one multilingual product page -> draft inquiry reply.
30-day product: product library, templates, team accounts, review workflow, history, and usage tracking.
Private deployment: install inside the factory, connect enterprise WeChat or email, and provide annual support.
```

The response must identify the smallest paid pilot and avoid building a general-purpose content platform first.
