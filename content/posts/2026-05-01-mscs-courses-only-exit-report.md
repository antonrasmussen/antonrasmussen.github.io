---
title: 'MSCS Courses-Only Exit Report'
date: 2026-05-01
source: odu_ms_exit
status: published
visibility: public
section: research
tags: [education, CS, career]
---

## Master of Science in Computer Science — Courses-Only Exit Report

**Anton Rasmussen**  
Old Dominion University - Department of Computer Science  
Spring 2026

---

## 1. Introduction

I am a Senior Data Engineer working in healthcare data systems. Before starting the MSCS at Old Dominion University, I had strong practical experience in ETL, distributed systems, and cloud data platforms, but I wanted a deeper theoretical foundation and stronger AI/ML depth. My goal was to improve both technical judgment and communication with research-oriented teams.

Across thirteen graduate courses from Spring 2024 to Spring 2026, I developed stronger foundations in algorithms and architecture, broadened my data and AI toolkit, and gained a clearer framework for secure and responsible deployment. This report summarizes what I learned in each course, how I applied it to professional work, recommendations for program improvement, and my overall impression of the program.

---

## 2. Foundations in Computer Science

### 2.1 Algorithms and Data Structures (CS 600)

CS 600 gave me a rigorous framework for reasoning about efficiency and correctness. The most valuable outcomes were disciplined complexity analysis, clearer understanding of when to use dynamic programming versus greedy strategies, and stronger fluency with graph-based reasoning.

I apply this directly when designing production pipelines. Instead of treating performance as trial-and-error tuning, I now start with complexity assumptions and expected bottlenecks, then validate them with profiling. This course changed my approach from tool-first debugging to principle-first design.

### 2.2 Computer Architecture (CS 665)

CS 665 helped me connect software behavior to hardware constraints through CPI, Amdahl's Law, caching, and pipeline behavior. The course made performance tradeoffs more concrete, especially the limits of local optimizations when the dominant cost is elsewhere in the system.

In practice, this changed how I explain system behavior to engineering teams. I now frame performance issues as compute-bound versus memory-bound phases and can justify architectural choices with clearer evidence. The main takeaway is that performance conversations are far more productive when grounded in architecture, not intuition.

---

## 3. Data Science and Large-Scale Data Systems

### 3.1 Intro to Data Science & Analytics (CS 620)

CS 620 established my baseline data science workflow: data cleaning, exploratory analysis, model evaluation, and interpretation. The course was especially useful for reinforcing metric literacy and linking model results to decision quality rather than headline accuracy alone.

I applied this mindset in my work by standardizing how I report model quality and by being more explicit about tradeoffs between precision, recall, and operational impact. The largest practical gain was consistency in how I move from raw data to decision-ready outputs.

### 3.2 Data Analytics and Big Data (CS 624)

CS 624 expanded my capabilities from analysis to scalable systems, especially Spark-based processing, streaming concepts, and lakehouse-oriented design. The course also connected modern ML workflow concerns to data engineering practice.

Professionally, this course strengthened my ability to design data platforms that support both analytics and ML workloads without separate, fragile pipelines. I now evaluate architecture choices more explicitly around maintainability, observability, and cost at scale.

### 3.3 High Performance Computing for Big Data (CS 724)

CS 724 provided hands-on depth in distributed and parallel computing, including Hadoop, Spark, and GPU-oriented thinking. The most important outcome for me was learning how to combine system-level tools with practical experimentation under realistic constraints.

My final project built a Spark-based de-identification pipeline for healthcare XML data with masking and encryption workflows. That work maps closely to my professional environment, where privacy protection and scalable processing are simultaneous requirements. This course improved my confidence in implementing privacy-aware pipelines, not just discussing them conceptually.

### 3.4 Data Mining and Security (CS 773)

CS 773 strengthened my understanding of applied data mining workflows, especially model selection, evaluation, and preprocessing decisions in security-related contexts. The course was valuable because it emphasized how small preprocessing choices can strongly affect downstream model behavior.

I use that lesson in production reviews by spending more time on data quality and feature assumptions before debating model algorithms. The course reinforced a practical truth: many model failures are data pipeline failures in disguise.

### 3.5 Data Visualization (CS 625)

CS 625 improved how I communicate technical findings to non-technical stakeholders. The strongest contribution was a structured approach to matching visual form to analytic question, then validating whether the chart supports an honest interpretation.

I applied this in healthcare reporting workflows where clarity matters as much as technical correctness. I now design visual outputs with explicit audience and decision context in mind, which has improved both stakeholder trust and adoption of analytics results.

---

## 4. Artificial Intelligence and Machine Learning

### 4.1 Generative AI (CS 795)

CS 795 combined generative model fundamentals with practical deployment workflows. The key gain was not just understanding transformer-based systems, but learning how model lifecycle decisions affect reliability, privacy, and operational feasibility.

In my work, this changed how I evaluate cloud-first versus edge-capable deployment paths. I now treat deployment design as part of model quality, especially in regulated settings where data governance and latency constraints can outweigh raw benchmark gains.

### 4.2 AI Security & Privacy (CS 695)

CS 695 made adversarial robustness concrete through hands-on attack and defense work. The most important lesson was that high clean accuracy does not imply security, and that subtle data or model manipulations can pass unnoticed without deliberate testing.

I now approach ML deployment reviews with a stronger threat-model mindset. This includes asking earlier questions about poisoning risk, integrity checks, and defense planning rather than treating security as a post-deployment concern.

### 4.3 Trustworthy Health Analytics (CS 581)

CS 581 connected healthcare analytics to fairness, explainability, and governance requirements. The course clarified how bias and representational gaps can enter a pipeline long before final model evaluation.

I apply this by including fairness and explainability checks in model review conversations, especially for healthcare-related use cases. The main shift was moving from "does it predict well?" to "is it acceptable, auditable, and equitable in context?"

### 4.4 AI for Health Sciences (CS 781)

CS 781 linked biomedical AI tasks to deployment-quality evaluation. The most useful part for me has been the emphasis on calibration and behavioral stability, not just aggregate accuracy, in settings where incorrect confidence can carry high consequences.

This directly informs how I assess model readiness in healthcare contexts. A practical limitation I observed is that the course covered many advanced topics quickly; additional depth on clinical implementation workflows would make the transition from prototype to deployment even stronger.

---

## 5. Web Security (CS 533)

CS 533 covered core web security risks and defensive patterns relevant to any system with browser-facing or API-facing components. The hands-on labs made common issues such as session handling mistakes, cross-site attacks, and policy misconfiguration more tangible than lecture-only coverage.

I apply these lessons when reviewing internal tools and data platform interfaces, especially where authentication and session behavior affect protected data access. Together with AI security and fairness coursework, CS 533 helped me build a more complete view of trustworthy systems from infrastructure through model behavior.

---

## 6. Colloquium (CS 690)

CS 690 exposed me to current research and industry perspectives beyond the scope of individual course assignments. The main benefit was seeing how researchers and practitioners frame problems, communicate evidence, and justify tradeoffs.

That broader exposure helped me contextualize my coursework and sharpened how I discuss technical decisions with mixed audiences. It also clarified which areas of AI and data engineering I want to pursue after graduation.

---

## 7. Application to Professional Work

The most important change from this degree is that I now approach work with stronger integration across algorithms, systems, and responsible AI principles. In practice, I make architecture decisions with clearer complexity and hardware assumptions, then validate them through profiling and operational metrics rather than ad hoc tuning.

For machine learning work, I now evaluate readiness across a wider set of criteria: model quality, data quality, security exposure, fairness risk, and confidence reliability. This has made my collaboration with data scientists and stakeholders more effective because I can discuss tradeoffs in a shared technical language rather than from a single engineering perspective.

For healthcare-focused projects, the program gave me a practical framework for balancing scale, compliance, and trust. I leave the program better prepared to design systems that are not only performant, but also secure, explainable, and realistic to maintain in production settings.

---

## 8. Suggestions for Program Improvement

Based on my experience, I suggest the following improvements.

**1) Add a dedicated production ML/MLOps course.**  
Students currently assemble these skills across multiple classes. A focused course on model lifecycle management, deployment standards, monitoring, and drift response would better prepare graduates for industry practice.

**2) Expand cloud-native and platform engineering coverage.**  
Structured coverage of containerization, infrastructure automation, CI/CD, and reproducibility would close a recurring gap between academic prototypes and production systems.

**3) Increase industry-facing practicum options.**  
More structured collaboration with external partners would improve student exposure to real constraints, including compliance, stakeholder alignment, and long-lived system ownership.

**4) Strengthen interdisciplinary pathways for health applications.**  
Joint activities with health and biomedical programs would improve problem framing and domain realism for students interested in clinical and public-health analytics.

---

## 9. Overall Reflection

The ODU MSCS program was a meaningful step in my professional development. I entered with strong implementation experience but uneven theoretical depth; I leave with a more balanced foundation across algorithms, systems, data science, and AI. The program improved not only what I can build, but how I reason about tradeoffs and communicate decisions.

A consistent theme across my coursework was applying computing methods to healthcare contexts, and that focus clarified my long-term direction. At the same time, balancing full-time work with graduate study was demanding, and some terms required prioritizing breadth over depth. Even with that constraint, the program delivered clear value and has prepared me to take on more advanced technical leadership in secure and trustworthy AI-enabled data systems.
