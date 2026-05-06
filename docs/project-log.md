
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
