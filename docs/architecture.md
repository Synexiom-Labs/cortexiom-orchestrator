# Architecture — Cortexiom Orchestrator

## Overview

The Cortexiom Orchestrator is a multi-agent compliance evaluation system that demonstrates Cortexiom as a **reasoning supervisor** over a standard document-parse → evidence-gather → recommend pipeline. It uses Google ADK 2.0 and Gemini 2.5 Flash for orchestration, with Cortexiom as an external reasoning service called at three critical checkpoints.

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Streamlit Demo Frontend                      │
│           (side-by-side: baseline vs. supervised)               │
└─────────────────────────┬───────────────────────────────────────┘
                          │
          ┌───────────────┴────────────────┐
          │                                │
          ▼                                ▼
┌─────────────────┐              ┌──────────────────────┐
│ workflow/        │              │ workflow/             │
│ baseline.py     │              │ supervised.py         │
│                 │              │                       │
│ 1. Parse reg    │              │ 1. Parse reg          │
│ 2. Gather ev.   │              │ 2. Gather evidence    │
│ 3. Draft rec.   │              │ 3. ━━━ CP1 ━━━━━━━━  │
│                 │              │ 4. Draft recommendation│
│                 │              │ 5. ━━━ CP2 ━━━━━━━━  │
│                 │              │ 6. Revise recommendation│
│                 │              │ 7. ━━━ CP3 ━━━━━━━━  │
└─────────────────┘              └──────────────────────┘
          │                                │
          └───────────────┬────────────────┘
                          │
                          ▼
                ┌─────────────────┐
                │  Gemini 2.5     │
                │  Flash (LLM)    │
                │  via Google ADK │
                └─────────────────┘

                   CP1 / CP2 / CP3
                          │
                          ▼
                ┌─────────────────────────────────┐
                │    Cortexiom API                │
                │    POST /v1/encounter           │
                │                                 │
                │  Input:  message + state_token  │
                │  Output: response + confidence  │
                │          depth + state_token    │
                │                                 │
                │  Wisdom Architecture:           │
                │  Observer → Hypothesis →        │
                │  Contradiction → Calibration →  │
                │  Reflection                     │
                └─────────────────────────────────┘
```

---

## Agent Architecture (ADK)

```
agent.py
  └── root_agent = coordinator (LlmAgent)
        ├── AgentTool: document_parser (LlmAgent)
        │     └── tools: read_regulation(), list_regulations()
        ├── AgentTool: evidence_gatherer (LlmAgent)
        │     └── tools: search_knowledge_base(), get_document(), list_knowledge_base()
        │               [optional: VertexAISearchTool if configured]
        └── AgentTool: recommendation_drafter (LlmAgent)
              └── tools: (none — synthesis only)
```

---

## Cortexiom State Token Flow

The `state_token` is held in Python memory as a local variable. It is never stored in a database or external system. Cortexiom API returns a new token with each call; the Python code passes it to the next call, enabling session continuity across three checkpoints within one workflow execution.

```
CP1 call → returns state_token_1
CP2 call (with state_token_1) → returns state_token_2
CP3 call (with state_token_2) → returns state_token_3
```

This is consistent with the "zero state custody" design: the token is an opaque AES-256-GCM encrypted blob even when Synexiom Labs is both the API provider and the developer building the orchestrator.

---

## Data Architecture

```
data/
├── regulations/          ← 5 synthetic regulatory documents
│   ├── edd_regulation.md
│   ├── data_residency_policy.md
│   ├── hie_consent_regulation.md
│   ├── advisor_conflict_disclosure.md
│   └── cross_border_data_transfer.md
├── knowledge_base/       ← 5 synthetic org documents (evidence_gatherer searches here)
│   ├── pep_client_records.md
│   ├── data_residency_posture.md
│   ├── hie_operations.md
│   ├── advisor_compensation.md
│   └── cross_border_inventory.md
└── adverse_flags/        ← 1 restricted flags document (NOT in evidence_gatherer scope)
    └── pep_adverse_flags.md
```

The `adverse_flags/` directory is intentionally outside `evidence_gatherer`'s search scope. For the PEP EDD test case, this creates the structural flaw that Cortexiom surfaces at CP1.

---

## Deployment

```
Cloud Run (cortexiom-orchestrator)
  └── Container: gcr.io/cortexiom-orchestrator/cortexiom-orchestrator
        ├── Streamlit frontend on :8080
        ├── Secrets via Secret Manager (CORTEXIOM_API_KEY, GOOGLE_API_KEY)
        └── Data files bundled in container image

GCS Bucket (cortexiom-orchestrator-data)
  └── compliance-data/     ← uploaded by scripts/setup_gcs.py
        ├── regulations/
        ├── knowledge_base/
        └── adverse_flags/

Optional: Vertex AI Search
  └── data store pointing at GCS compliance-data/
      enables semantic search in evidence_gatherer
```

---

## Technology Stack

| Component | Technology |
|---|---|
| LLM | Gemini 2.5 Flash (via Google AI / Vertex AI) |
| Agent framework | Google ADK 2.0 |
| Reasoning supervisor | Cortexiom API (Wisdom Architecture) |
| Frontend | Streamlit |
| Storage | Google Cloud Storage |
| Optional search | Vertex AI Search |
| Deployment | Cloud Run |
| Language | Python 3.11 |