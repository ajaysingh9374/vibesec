# VibeSec

VibeSec is an academic cybersecurity prototype exploring AI-assisted security assessment workflows for Security Operations Center (SOC) contexts.

## Project Scope

The project investigates how AI can support vulnerability assessment and threat modelling by:

- automating vulnerability scanning through established tools,
- parsing and interpreting scan results,
- applying AI-assisted threat modelling, and
- producing structured security assessment reports.

## Research Context

This project is developed as a postgraduate-level proof of concept under the theme:

**When AI Meets the SOC: Automating Vulnerability Assessment and Threat Modelling**

During development and testing, simulated scan outputs are used. Live execution is planned for a later phase in a controlled cyber lab environment.

## SMART Project Objectives

1. **Automated Nmap XML Ingestion and Parsing (Specific/Measurable/Achievable/Relevant/Time-bound)**  
   By **June 30, 2026**, implement and validate a pipeline that ingests Nmap XML outputs and extracts core host, port, service, and vulnerability-indicative findings with at least **95% field-level parsing accuracy** on a supervised test set.

2. **AI-Assisted Threat Modelling with Human Validation (Specific/Measurable/Achievable/Relevant/Time-bound)**  
   By **July 31, 2026**, produce AI-assisted threat models for scan-derived findings and complete **human-in-the-loop review for 100% of modelled cases**, with reviewer disposition (accept/revise/reject) recorded for traceability.

3. **Structured Security Assessment Report Generation (Specific/Measurable/Achievable/Relevant/Time-bound)**  
   By **August 31, 2026**, generate a repeatable structured assessment report format that includes scope, technical findings, threat model outputs, prioritised risks, and recommendations, with **100% section completeness** across at least **five simulated assessment runs**.

4. **Demonstration of Supervised Vibe Computing Workflow (Specific/Measurable/Achievable/Relevant/Time-bound)**  
   By **September 15, 2026**, demonstrate an agentic AI co-development workflow evidenced by a maintained project log and GitHub history containing at least **20 meaningful commits** that document iteration, reviewer feedback, and decision rationale.

5. **Controlled Live Lab Execution (Optional) (Specific/Measurable/Achievable/Relevant/Time-bound)**  
   By **October 31, 2026** *(subject to supervisor approval and lab readiness)*, conduct at least **one controlled live lab execution** to compare live and simulated outputs, and document observed variance, operational constraints, and risk controls.

## Repository Structure

```text
vibesec/
├── docs/
│   └── README.md
├── reports/
│   └── README.md
├── src/
│   └── README.md
└── README.md
```

- `src/`: Python source modules and workflow logic.
- `docs/`: Project documentation and design notes.
- `reports/`: Security assessment outputs and reporting artifacts.
