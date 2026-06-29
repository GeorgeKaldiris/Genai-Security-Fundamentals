# GenAI Security Fundamentals

This repository contains my personal study notes and practical examples on Generative AI Security fundamentals.

The goal of this project is to understand and explain the main security risks of Large Language Model applications, based mainly on the OWASP Top 10 for LLM Applications and connect them with practical controls used in Cyber AI, AI Security and GenAI Governance roles.

This repository is part of my learning path toward junior Cyber AI / AI Security roles.

## Repository structure

```text
Genai-Security-Fundamentals/
│
├── README.md
│
├── docs/
│   ├── 01-prompt-injection.md
│   ├── 02-sensitive-data-disclosure.md
│   ├── 03-improper-output-handling.md
│   ├── 04-ai-governance.md
│   ├── 05-data-and-model-poisoning.md
│   ├── 06-supply-chain-risks.md
│   └── 07-how-to-secure-a-company-genai-tool.md
│
└── examples/
    └── mask_logs_example.py
```

## Topics covered

### 1. Prompt Injection

Prompt injection is a risk where user input or external content manipulates the behavior of a Large Language Model.

This topic covers direct and indirect prompt injection, jailbreaking, RAG-related risks and basic mitigations such as input validation, least privilege, access control, monitoring and human approval for high-risk actions.

File:

```text
docs/01-prompt-injection.md
```

### 2. Sensitive Data Disclosure

Sensitive data disclosure happens when private, confidential or protected information enters or exits a GenAI system in an unsafe way.

This topic covers risks related to personal data, raw logs, API keys, tokens, credentials, confidential business documents, source code and internal system information.

File:

```text
docs/02-sensitive-data-disclosure.md
```

### 3. Improper Output Handling

Improper output handling happens when an application trusts LLM-generated output without proper validation, sanitization, encoding or review before passing it to another system.

This topic covers risks such as XSS, SQL injection, unsafe database operations, path traversal, unsafe code execution and unsafe backend actions.

File:

```text
docs/03-improper-output-handling.md
```

### 4. AI Governance

AI Governance is the set of policies, roles, processes, responsibilities and technical controls that define how AI systems are used safely and responsibly inside an organization.

This topic connects GenAI security with governance concepts such as acceptable use policies, access control, data classification, monitoring, risk assessment, accountability and continuous improvement.

File:

```text
docs/04-ai-governance.md
```

### 5. Data and Model Poisoning

Data and model poisoning happens when attackers manipulate training data, fine-tuning data, embeddings, RAG knowledge bases or model behavior in order to influence the output of an AI system.

This topic covers poisoning risks in pre-training, fine-tuning, embeddings, RAG systems and model integrity.

File:

```text
docs/05-data-and-model-poisoning.md
```

### 6. Supply Chain Risks in LLM Applications

Supply chain risks in LLM applications come from third-party components used to build, train, fine-tune, deploy or operate GenAI systems.

This topic covers risks related to third-party models, datasets, Python libraries, APIs, cloud AI services, LoRA adapters, model repositories and unclear provider policies.

File:

```text
docs/06-supply-chain-risks.md
```

### 7. How to Secure a Company GenAI Tool

This note combines the previous topics into one practical scenario.

It explains how to secure an internal company GenAI assistant that uses corporate data, documents, logs, APIs or RAG knowledge bases.

It covers access control, data masking, input and output validation, RAG security, least privilege, monitoring, human approval, supply chain review and AI Governance.

File:

```text
docs/07-how-to-secure-a-company-genai-tool.md
```

## Practical example

The repository also includes a simple Python example that demonstrates basic masking of sensitive data before using logs in a GenAI workflow.

The script detects and masks examples of sensitive information such as:

* email addresses;
* bearer tokens;
* API keys;
* IP addresses.

File:

```text
examples/mask_logs_example.py
```

This is not a production-ready Data Loss Prevention solution. It is an educational example that shows the idea that raw logs should not be sent directly to an LLM without masking, filtering or data minimization.

## How to run the Python example

```bash
python examples/mask_logs_example.py
```

Expected idea:

```text
Raw log:
User john@example.com failed login from 192.168.1.25 with Authorization: Bearer abc123.secret.token and api_key=sk_test_12345

Masked log:
User [EMAIL_MASKED] failed login from [IP_MASKED] with Authorization: Bearer [TOKEN_MASKED] and api_key=[API_KEY_MASKED]
```

## Why this matters

GenAI tools can improve productivity, automate security workflows, support SOC analysts, summarize logs, assist with phishing analysis and help organizations work faster.

However, they also introduce risks related to prompt injection, sensitive data exposure, unsafe outputs, poisoned data, untrusted models, supply chain dependencies, hallucinations and lack of governance.

Secure GenAI design requires controls around the model, the data, the user input, the model output, connected tools and organizational processes.

## Key lessons learned

The most important lessons from this project are:

* LLM input should be treated as untrusted.
* LLM output should also be treated as untrusted.
* Raw logs and sensitive company data should not be sent to LLMs without masking or controls.
* GenAI tools should follow least privilege and role-based access control.
* RAG systems should not blindly trust retrieved documents.
* Third-party models, datasets, libraries, APIs and cloud services should be verified before use.
* Data quality and model integrity are important security concerns.
* AI Governance is needed to define rules, responsibilities, monitoring and accountability.


## References

* OWASP Top 10 for LLM Applications
* NIST AI Risk Management Framework
* ISO/IEC 42001 Artificial Intelligence Management System
* EU AI Act overview

