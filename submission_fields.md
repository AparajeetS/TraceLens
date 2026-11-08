# Apart Research Swarm Alignment Hackathon: Submission Fields

Use this reference to complete the official submission form at:
https://apartresearch.com/sprints/swarm-alignment-2026 (click **"Submit your project"**)

---

### 1. Project Details

- **Project title:**  
  `TraceLens-Gateway: Multi-Agent Oversight from Covert Communication Detection to Action-Slicing Interception`

- **Project summary (Abstract: 198 words, satisfies 150–250 word requirement):**  
  ```text
  When autonomous AI agents interact, negotiate, and share tools in large swarms, centralized monitors face a compounding dual vulnerability: communication logs are heavily fragmented by network attrition, and malicious workflows are strategically sliced across distinct agents to bypass isolated review filters. We introduce TraceLens-Gateway, an end-to-end multi-agent oversight system addressing both failure modes. At the telemetry layer, TraceLens implements a masked recurrence monitor that detects low-frequency rendezvous tokens across lossy streams, maintaining 86.2% recall even when 50% of messages are dropped, while uncalibrated frequency filters suffer prohibitive false-alarm rates (up to 73.0% false positives). At the execution layer, TraceLens-Gateway introduces an Action-Dependency Directed Acyclic Graph (DAG) that reconstructs cross-agent causal taint to intercept request-slicing attacks. In an empirical benchmark of 30 multi-agent attacks spanning DevOps privilege staging, Cloud IAM escalation, and structured financial threshold evasion, isolated single-request review suffers a 100% bypass rate and rolling time windows fail at 66.7%, whereas our causal DAG intercepts 100% of sliced attacks (0% bypass) with 0.0% false alarms on benign collaborative workflows. Grounded in empirical incident traces from the recent OpenAI–Hugging Face evaluation breach, our findings demonstrate that robust swarm alignment requires linking statistical communication surveillance with stateful causal action gating.
  ```

- **PDF report:**  
  Upload file: `report_unified.pdf` (8 pages, balanced ~90% vertical fill per page, zero dead whitespace, fully compliant with Apart template & rubric, under 25 MB).  
  *(Alternative standalone 3-page telemetry paper is also available at `report.pdf` if preferred)*

- **Are you interested in publishing this project?**  
  Select: `Yes` (recommended for fellowship/grant considerations)

- **Tracks:**  
  Primary: ☑ `Track 4: Multi-Agent Oversight and Control`  
  Secondary: ☑ `Track 2: Emergent Coordination / Defenses`

- **Presentation recording:**  
  *Leave blank* (unless you recorded a 3-5 min video)

- **Project code:**  
  *Leave blank* or provide GitHub repo URL if you host it. The complete source code is packaged in `TraceLens_source.zip`.

- **Slides:**  
  *Leave blank* (optional)

- **Project image:**  
  Upload file: `results/gateway_results.png` (high-resolution composite plot showing attack bypass vs detection rates across threat domains)

- **Additional material:**  
  *Leave blank* (optional)

---

### 2. Team Details (User-specific fields to fill in form)

- **Team name:**  
  `TraceLens` (or your preferred team name)

- **Location:**  
  `Online` (or your City)

- **Team member 1:**  
  - **Name:** Aparajeet Shadangi
  - **Email:** *[Your Email Address]*
  - **Discord username:** *[Your Discord handle, optional]*
  - **Google Scholar profile:** *[Optional]*

---

### Pre-Submission Verification Checklist

- [x] Report PDF under 8-page maximum (exactly 8 pages, balanced vertical fill per page, zero dead whitespace)
- [x] Project summary / Abstract between 150 and 250 words (198 words)
- [x] Author names and affiliations section present
- [x] Grounding in empirical incident traces (*vopi/OpenAI-HF-Hack-SwarmTraces*, SwarmTraces.org)
- [x] Mandatory Appendix: "Limitations and Dual-Use / Ethical Considerations" present
- [x] LLM Usage Statement included
- [x] Figure 1 and Figure 2 embedded cleanly alongside Table 1 and Table 2
- [x] Clean typographic hierarchy, zero raw LaTeX escape artifacts
- [x] Fully reproducible code with deterministic seed (runs in <3s locally)
