# VibeSec: AI-Assisted Security Assessment System

## CyberLab Security Assessment Report

---

**Student Name:** Ajay Singh  
**Module:** CI7530 - CyberSecurity and Artificial Intelligence  
**Project:** VibeSec (AI-Assisted Threat Modelling System)  
**Assessment Type:** Security Assessment using AI-supported methodology  
**Date:** May 2026  

---

**Description:**

This report presents the output of VibeSec, a structured and stage-driven security assessment system that integrates network scanning, threat context mapping, and AI-assisted reasoning. The objective is to demonstrate how artificial intelligence can support cybersecurity analysis while maintaining clear boundaries, transparency, and human oversight.

---
## SMART Project Objectives

1. **Parse Nmap XML scan outputs into structured security evidence**  
   By the project submission deadline, implement a Python-based parsing workflow that ingests Nmap XML outputs and extracts hosts, ports, protocols, service names, versions, states, and relevant script output into a structured intermediate format. Success will be measured by achieving at least **95% field-level extraction accuracy** against a small manually checked test set, with parsing failures recorded and explained in the project log.

2. **Produce AI-assisted threat models with explicit human validation**  
   By the completion of the prototype assessment workflow, use AI assistance to transform parsed scan evidence into threat model entries covering likely attack paths, affected assets, threat actors, assumptions, and mitigations. Each AI-generated threat model must be reviewed by a human validator, with **100% of entries marked as accepted, revised, or rejected** so that the final output demonstrates accountable human-in-the-loop governance rather than unverified automation.

3. **Generate automated security assessment reports from structured findings**  
   By the final implementation milestone, develop an automated reporting component that converts parsed scan data and validated threat model outputs into a professional security assessment report. The report must include scope, methodology, technical findings, prioritised risks, recommended mitigations, limitations, and evidence references, with **all required sections present in at least five repeatable test runs**.

4. **Demonstrate a vibe-computing and agentic AI development workflow using GitHub evidence**  
   Throughout the coursework period, maintain GitHub evidence showing how agentic AI support was used to plan, scaffold, refine, and document the project. The workflow will be considered successful if the repository contains a coherent commit history, project log updates, prompt artefacts, and implementation changes that demonstrate at least **four distinct AI-supported development iterations** with visible human review or decision-making.

5. **Optionally validate the workflow through controlled live lab execution**  
   If time and lab conditions permit before submission, conduct at least **one controlled live execution** against an authorised lab target to compare live scan-derived outputs with simulated or sample-based outputs. The exercise must document the target scope, safety controls, observed differences, operational constraints, and any ethical or legal limitations, ensuring that live testing remains proportionate, authorised, and reproducible.

## Prompt Design Parameters Used in VibeSec

Good prompts were used to keep the AI support focused, practical, and safe for a cybersecurity coursework project. The table below records the main prompt parameters used when planning and building VibeSec.

| Prompt parameter | Why it is important | Example from VibeSec |
| --- | --- | --- |
| Clear role | Tells the AI what type of expertise to apply and keeps the response relevant. | "Act as a cybersecurity student building a small AI-assisted vulnerability reporting tool." |
| Specific task | Makes the expected work clear and reduces vague or unfocused output. | "Create SMART objectives for a project that parses Nmap XML and generates a security report." |
| Project context | Helps the AI understand the purpose, audience, and coursework requirements. | "This is for CI7530 CyberSecurity and Artificial Intelligence coursework using VibeSec as the prototype." |
| Input evidence | Grounds the AI output in real project material rather than guessing. | "Use Nmap XML fields such as hosts, ports, services, states, and script output as the source evidence." |
| Output format | Makes the result easier to review, reuse, and include in documentation or reports. | "Return the answer as a Markdown table with finding, risk, evidence, and mitigation columns." |
| Constraints | Prevents unwanted changes and keeps the response within the project scope. | "Do not change code or folder structure; only update docs/project-log.md." |
| Safety and ethics | Important in cybersecurity work because prompts must avoid unauthorised or harmful activity. | "Only describe testing against authorised lab targets and include limitations and human validation." |
| Validation request | Encourages the AI to include checks, assumptions, and areas needing human review. | "Mark AI-generated threat model entries as accepted, revised, or rejected after human review." |
| Practical examples | Makes the prompt output easier to understand and apply in the project. | "Show an example mitigation for an open service discovered in an Nmap scan." |

## Stage 2 Threat Modelling Scope

Stage 2 defines the planned threat modelling boundary for VibeSec. This stage is planning and scoping only. It does not add automated threat logic, vulnerability scoring, exploitation, reporting, or AI calls.

### Purpose

The purpose of Stage 2 is to prepare a simple threat modelling approach that can use the structured evidence produced in Stage 1. The focus is on high-level exposure only, such as which hosts, open ports, protocols, services, and versions are visible from the parsed Nmap XML data.

Stage 2 does not decide whether a system is vulnerable. It only defines how later threat modelling suggestions should be framed and controlled.

### Inputs

Stage 2 will use the parsed data from Stage 1, including:

- host IP addresses and hostnames
- open ports
- protocols such as TCP or UDP
- service names
- service versions, where available

The source evidence for this stage is the parsed output from Nmap XML files such as `reports/localhost_nmap.xml`.

### Threat Modelling Focus

Threat modelling in Stage 2 will reason only about high-level exposure. This means it may describe what is externally visible or available based on the parsed scan evidence.

Examples of acceptable high-level focus areas include:

- which services are exposed
- which hosts have open ports
- how many open services are present
- whether service information is available or unknown
- what assumptions would need human review before any conclusion is made

This stage must remain descriptive. It must not claim that an exposed service is vulnerable without later validation.

### Expected Outputs

Stage 2 is expected to produce a clear threat modelling structure that can later be used for human-reviewed suggestions. Possible outputs include:

- a list of observed hosts and exposed services
- high-level exposure notes
- assumptions that require human checking
- confidence or review status fields such as "needs review", "accepted", "revised", or "rejected"
- clear warnings where content is AI-generated

These outputs are preparation for later work. They are not final security findings and are not a report.

### Role of AI

AI may be used in Stage 2 only as an assistance or suggestion tool. AI output must not be treated as a final decision.

Any AI-generated content must include a clear warning such as:

> Warning: This content was AI-generated and must be reviewed by a human before use.

Final judgement always remains with a human assessor. The human reviewer must decide whether AI-generated suggestions are accepted, revised, or rejected.

### Out of Scope

The following activities are explicitly out of scope for Stage 2:

- exploitation or exploit attempts
- vulnerability scoring
- CVE database lookups
- automated security recommendations
- final reporting
- automated AI reasoning or AI API calls
- replacing human judgement

Reporting is not part of Stage 2. Reporting belongs to Stage 3.

## Stage 2 Step 2.2: Mapping Parsed Findings to Threat Context

This step maps parsed scan data to broad threat context in a human-readable way. It is not an automated threat model, not an AI-generated conclusion, not a risk assessment, and not a report.

The purpose is to explain what general kind of exposure a technical finding may relate to, so that a human reviewer has a clear starting point for later threat modelling.

### Mapping Principles

- Use only parsed Stage 1 scan data: hosts, open ports, protocols, services, and versions.
- Keep wording generic and descriptive.
- Do not assign severity, likelihood, or impact.
- Do not use CVE databases or vulnerability scoring.
- Do not recommend fixes at this stage.
- Treat all mappings as context notes requiring human review.

### High-Level Mapping Table

| Parsed technical finding | Possible threat category | Simple explanation |
| --- | --- | --- |
| Host with one or more open ports | Network exposure | A host with open ports has services reachable on the network. |
| Open TCP service | Service exposure | An open TCP service may allow remote systems to connect to that service. |
| Open UDP service | Datagram-based service exposure | An open UDP service may indicate a service that communicates without a persistent connection. |
| Open SMB or file-sharing service | Network file-sharing surface | An open SMB or file-sharing service increases exposure to network-based threats. |
| Open remote administration service | Remote access surface | A remote administration service may provide an access path that requires careful human review. |
| Open web service | Web surface | An exposed web service may present a web application or HTTP-based attack surface. |
| Open database service | Data service surface | A database service exposed on the network may relate to data access or storage exposure. |
| Open directory or identity service | Identity and authentication surface | Directory or identity services may relate to authentication, user lookup, or domain services. |
| Open mail service | Messaging surface | A mail service may expose email transport or mailbox-related functionality. |
| Unknown service name or version | Unclear exposure | Missing service details mean the exposure needs human review before conclusions are made. |
| Multiple open services on one host | Broader host exposure | A host with several open services has more visible network functions to review. |

### Example Using Current Parsed Data

The current parsed localhost scan contains open TCP services including `msrpc`, `microsoft-ds`, and `wsdapi`. At this stage, these are mapped only to possible high-level contexts:

| Parsed service | Possible threat context | Notes |
| --- | --- | --- |
| `msrpc` on TCP port `135` | Remote service communication surface | This indicates a reachable RPC-related service. No vulnerability conclusion is made. |
| `microsoft-ds` on TCP port `445` | Network file-sharing or Windows networking surface | This indicates a reachable SMB-related service. No severity or risk score is assigned. |
| `wsdapi` on TCP port `5357` | Service discovery or web-services device surface | This indicates a reachable service discovery-related endpoint. No recommendation is made at this step. |

### Boundary Statement

This mapping is descriptive only. It does not confirm that a threat exists, does not prove exploitability, and does not decide whether a service is safe or unsafe. Final interpretation must remain with a human reviewer in a later Stage 2 activity.

## Stage 2 Step 2.3: AI-Assisted Threat Reasoning

This step documents how AI assistance may be used to suggest possible threat interpretations from the Stage 2.2 threat context mapping. It remains advisory only. It does not create a report, does not declare vulnerabilities, and does not replace human judgement.

### Purpose

The purpose of Step 2.3 is to prepare high-level, human-reviewable threat interpretations from existing threat contexts such as network exposure, service exposure, web surface, and remote access surface.

This step keeps factual parsed data separate from AI-assisted interpretation. Parsed data remains evidence from Stage 1. Threat context remains the generic mapping from Step 2.2. AI-assisted text is only a suggestion for human review.

### Separation of Data, Context, and AI Reasoning

| Layer | What it contains | How it is treated |
| --- | --- | --- |
| Parsed data | Host, port, protocol, service, and version extracted from Nmap XML. | Factual technical input from Stage 1. |
| Threat context | High-level category from Step 2.2, such as network exposure or web surface. | Generic descriptive mapping. |
| AI-assisted interpretation | Suggested possible scenario based on the threat context. | Advisory only and explicitly labelled as AI-generated. |
| Human review | Human decision to accept, revise, or reject the suggestion. | Final authority before later use. |

### Rules for AI-Assisted Interpretations

- Every AI-generated statement must include an explicit warning.
- Wording must stay cautious, using terms such as "may", "could", or "might".
- The AI must not declare any host, service, or system vulnerable.
- The AI must not assign severity, likelihood, impact, or risk levels.
- The AI must not recommend mitigations or fixes.
- The AI must not reference CVEs or vulnerability databases.
- The AI must not replace human judgement.

### Advisory Interpretation Examples

| Threat context from Step 2.2 | AI-generated advisory interpretation | Human review status |
| --- | --- | --- |
| Network exposure | Warning: AI-generated. A host with reachable network services may provide a wider surface for later human review, depending on the intended role of the host and services. | Needs human review |
| Service exposure | Warning: AI-generated. An open service could represent a point where another system or user may interact with the host. This does not mean the service is vulnerable. | Needs human review |
| Network file-sharing surface | Warning: AI-generated. An SMB or file-sharing service may relate to shared resources or Windows networking functions that could be considered during later threat modelling. | Needs human review |
| Remote access surface | Warning: AI-generated. A remote access service might indicate an administrative or management pathway that should be understood in its operational context. | Needs human review |
| Web surface | Warning: AI-generated. An exposed web service may present a browser-accessible or HTTP-based interface that could be relevant to later threat modelling. | Needs human review |
| Data service surface | Warning: AI-generated. A database or data-related service may be relevant to later questions about data access paths, but this step does not assess weakness or exposure level. | Needs human review |
| Identity and authentication surface | Warning: AI-generated. A directory or identity-related service may be connected to authentication or user lookup functions and may need human context review. | Needs human review |
| Unclear exposure | Warning: AI-generated. If the service name or version is unknown, the exposure may need manual clarification before any later interpretation is accepted. | Needs human review |

### Example Based on Current Parsed Services

| Parsed data | Existing threat context | AI-generated advisory interpretation | Boundary note |
| --- | --- | --- | --- |
| `127.0.0.1`, TCP port `135`, service `msrpc` | Remote service communication surface | Warning: AI-generated. This may represent a reachable RPC-related communication service that could be considered during later high-level threat modelling. | No vulnerability conclusion is made. |
| `127.0.0.1`, TCP port `445`, service `microsoft-ds` | Network file-sharing or Windows networking surface | Warning: AI-generated. This may represent a reachable Windows networking or file-sharing service that could be relevant to later exposure review. | No severity, likelihood, or risk level is assigned. |
| `127.0.0.1`, TCP port `5357`, service `wsdapi` | Service discovery or web-services device surface | Warning: AI-generated. This may represent a reachable service discovery-related endpoint that could be noted as part of the visible service surface. | No mitigation or fix is recommended. |

### Human Review Requirement

All AI-assisted interpretations in Step 2.3 must be reviewed by a human before they are used in any later stage. The reviewer should mark each suggestion as accepted, revised, or rejected. Until that review happens, the content remains advisory preparation only.

### Boundary Statement

Step 2.3 prepares advisory material for future reporting but does not generate a report. It does not perform exploitation, vulnerability scoring, CVE lookup, mitigation planning, or final threat modelling decisions.

## Stage 3 Step 3.1: Report Scope and Audience Definition

Stage 3 begins the reporting stage for VibeSec. This step defines the purpose, scope, and intended audience of the future security assessment report. It does not generate the report itself.

### Report Purpose

The purpose of the VibeSec security assessment report is to present the outputs from earlier stages in a clear, structured, and reviewable format. The report will help a reader understand what was scanned, what technical data was extracted, what high-level threat context was mapped, and which AI-assisted interpretations require human review.

The report is intended to support assessment communication, not to prove exploitation or confirm vulnerabilities.

### Target Audience

The report is intended for a mixed audience:

- technical readers who need to understand scan evidence, open services, protocols, and extracted technical details
- academic readers who need to understand the project method, stage boundaries, and human-in-the-loop use of AI
- non-specialist security stakeholders who need a clear explanation of visible exposure without unsupported conclusions

The language should therefore be professional, clear, and structured. Technical details should be included, but they should be explained without assuming the reader is a penetration tester.

### Report Will Include

The future VibeSec report may include:

- assessment scope and source XML file reference
- Stage 1 scan and parsing results, including hosts, open ports, protocols, services, and versions
- simple Stage 1 summary counts, such as number of hosts and open ports
- Stage 2 threat context mappings, such as network exposure, service exposure, and web surface
- Stage 2 AI-assisted threat interpretations, clearly labelled as AI-generated and advisory
- human review status for AI-assisted content, such as needs review, accepted, revised, or rejected
- limitations and boundaries of the assessment

### Report Will Not Include

The report must not include:

- exploitation activity or exploit results
- confirmation that a system or service is vulnerable
- vulnerability scoring or severity ratings
- CVE lookups or vulnerability database references
- unsupported security conclusions
- remediation recommendations or fixes at this step
- new scanning, parsing, analysis, or threat modelling work

### Role of AI-Generated Content

AI-generated content may appear in the future report only as clearly labelled advisory material. It must be separated from factual parsed scan data and from human judgement.

Any AI-generated content included in the report must use a clear warning such as:

> Warning: This content was AI-generated and must be reviewed by a human before use.

AI-generated content must not be presented as a final finding. Human judgement remains the final authority, and the report should show whether AI-assisted content has been accepted, revised, rejected, or still needs review.

### Boundary Statement

Step 3.1 defines the report scope and audience only. It does not create the report, design the full report structure, generate findings, add recommendations, or introduce scoring. The next step will define the report structure.

## Stage 3 Step 3.2: Report Structure Design

This step defines the planned structure of the VibeSec security assessment report. It does not generate report content, findings, recommendations, CVEs, scores, or new analysis.

### Design Principles

- Keep the report simple, readable, and suitable for academic submission.
- Present factual scan data separately from threat context and AI-assisted interpretation.
- Label AI-generated content clearly and keep it advisory.
- Preserve human review as the final authority.
- Avoid exploitation, vulnerability confirmation, CVE references, scoring, and recommendations.

### Planned Report Sections

| Order | Report section | Purpose and planned contents |
| --- | --- | --- |
| 1 | Title Page | Identifies the report name, project name, assessment context, author, and date. |
| 2 | Executive Summary | Provides a short high-level overview of what the report covers, without detailed findings or recommendations. |
| 3 | Scope | Defines what was assessed, the source XML file, and the boundaries of the assessment. |
| 4 | Methodology | Explains the staged workflow used by VibeSec: scan input, XML parsing, simple summaries, threat context mapping, and AI-assisted advisory interpretation. |
| 5 | Parsed Scan Results | Presents factual Stage 1 data such as hosts, open ports, protocols, services, and versions. |
| 6 | Baseline Summary | Shows simple counts and groupings from Stage 1, such as total hosts, total open ports, and services discovered. |
| 7 | Threat Context Mapping | Presents Stage 2.2 mappings between parsed technical findings and high-level threat categories. |
| 8 | AI-Assisted Interpretation | Contains clearly labelled AI-generated advisory interpretations from Stage 2.3, separated from factual scan data. |
| 9 | Human Review Status | Records whether AI-assisted interpretations are pending review, accepted, revised, or rejected by a human reviewer. |
| 10 | Limitations | Explains what the assessment does not prove, including no exploitation, no vulnerability confirmation, no CVE lookup, no scoring, and no recommendations. |
| 11 | Appendix | Holds supporting material such as source file references, prompt notes, or structured tables if needed. |

### Logical Flow

The report should move from general context to technical evidence, then to advisory interpretation:

1. introduce the report and audience
2. define scope and methodology
3. show factual parsed scan data
4. summarise the factual data
5. map the data to high-level threat context
6. present AI-assisted advisory interpretation
7. record human review status
8. state limitations and boundaries

This ordering helps readers understand the difference between evidence, context, and advisory reasoning.

### Boundary Statement

Step 3.2 designs the report structure only. It does not populate the report, create final findings, perform new analysis, add recommendations, assign scores, or reference CVEs. The next step will focus on report content population within this structure.

### Conclusion

The VibeSec workflow demonstrates a structured and controlled approach to transforming network scan data into meaningful security assessment outputs. By separating factual evidence, high-level threat context, and AI-assisted interpretation, the system ensures clarity and avoids overclaiming.

The approach focuses on identifying system exposure rather than confirming vulnerabilities, aligning with a human-in-the-loop model where final judgement remains the responsibility of the reviewer. The use of AI in this process is deliberate and constrained, supporting analysis without replacing expert decision-making.

Overall, VibeSec illustrates how artificial intelligence can be responsibly integrated into cybersecurity workflows to improve understanding, consistency, and communication, while maintaining transparency and control.
