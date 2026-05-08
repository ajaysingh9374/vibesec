
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
