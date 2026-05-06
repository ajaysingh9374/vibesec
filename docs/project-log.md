
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
