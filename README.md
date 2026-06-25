# GenAI-Security-FundamentalS

This repository contains my personal study notes and practical examples on Generative AI Security fundamentals. The goal is to understand and explain the main risks of LLM-based applications, including prompt injection, sensitive data disclosure, improper output handling, data leakage and AI governance.

The content is based on the OWASP Top 10 for LLM Applications and focuses on practical explanations for junior Cyber AI / AI Security roles.

## Topics covered

- Prompt Injection
- Sensitive Data Disclosure
- Improper Output Handling
- Data Leakage
- AI Governance
- Protecting GenAI tools that use company data

## Practical example

The `examples/mask_logs_example.py` file shows a simple approach for masking sensitive information from logs before using them in a GenAI workflow.

## Why this matters

GenAI tools can improve productivity and security workflows, but they also introduce risks related to data exposure, malicious prompts, hallucinated outputs and unsafe integrations. Secure design requires controls around the model, the data, the user input, the output and the connected systems.
