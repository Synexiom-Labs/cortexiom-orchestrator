# Cortexiom Orchestrator
### Google for Startups AI Agents Challenge — 2026
**By Synexiom Labs**

A multi-agent compliance evaluation system that demonstrates **Cortexiom as a reasoning supervisor** over a standard document-parse → evidence-gather → recommend pipeline. Five test cases show how adding Cortexiom at three checkpoints catches what a baseline multi-agent workflow misses.

---

## What it demonstrates

A compliance team uses a multi-agent workflow to evaluate regulatory requirements:

1. **DocumentParser** — extracts rules from a regulation document
2. **EvidenceGatherer** — searches the organization's knowledge base
3. **RecommendationDrafter** — synthesizes a compliance recommendation

Without supervision, the pipeline produces **plausible but flawed** recommendations — it answers based on the evidence it retrieved, unaware of what it didn't retrieve, and unable to detect contradictions between regulatory standards and internal assumptions.

**Cortexiom adds three reasoning checkpoints:**

| Checkpoint | When | What it checks |
|---|---|---|
| **CP1 — Pre-decision** | After evidence gathered, before recommendation | Evidence completeness, missing sources, structural gaps |
| **CP2 — Post-recommendation** | After recommendation drafted | Contradictions, temporal gaps, jurisdiction-specific edge cases |
| **CP3 — Escalation** | Final step | Routing: file report / human review / urgent escalation |

The Cortexiom API returns `confidence`, `depth`, and `reasoning_trace` at each step. It holds session continuity via an encrypted `state_token` — no server-side state storage.

---

## Test Cases

| # | Scenario | What baseline misses | What Cortexiom catches |
|---|---|---|---|
| 1 | **PEP EDD Review** | 12 clients with missing SOF docs + 5 adverse media flags (in a directory outside evidence scope) | CP1: evidence scope limited to knowledge_base/ — adverse_flags/ not searched |
| 2 | **Data Residency** | Migration plan puts 4 production migrations in the same window as the compliance audit | CP2: Q1 2027 audit/migration conflict; interim control attestation overdue |
| 3 | **HIE Consent Audit** | Applies US opt-in form to Nova Scotia (PHIPA-NS permits implied consent) | CP2: PHIPA-NS s.23(1)(a) implied consent changes NS compliance posture entirely |
| 4 | **Advisor Disclosure** | Relies on 2023 legal opinion; 2024 CSA guidance tightened the standard after the opinion | CP2: legal opinion predates tightened regulation by 17 months — not reliable |
| 5 | **Cross-Border Transfer** | Notes Singapore as "planned" without flagging urgency | CP1: Singapore SCCs not executed; Q3 2026 start conflicts with 6-8 week SCC timeline |

---

## Architecture

```
Streamlit frontend
    │
    ├── workflow/baseline.py    ← Gemini 2.5 Flash, 3 stages, no supervision
    └── workflow/supervised.py  ← same 3 stages + Cortexiom at CP1, CP2, CP3

Cortexiom API (POST /v1/encounter)
    ← called 3x per supervised run
    ← state_token held in Python memory, passed between calls
    ← returns: response, confidence, depth, state_token

ADK Agents (for `adk run .`)
    └── coordinator (LlmAgent)
          ├── document_parser (LlmAgent + file tools)
          ├── evidence_gatherer (LlmAgent + file tools)
          └── recommendation_drafter (LlmAgent)
```

Full architecture diagram: [docs/architecture.md](docs/architecture.md)

---

## Setup

### Prerequisites

- Python 3.11+
- Google Cloud project with billing enabled
- Cortexiom API key (free tier: 50 encounters — get one at [developers.cortexiom.com](https://developers.cortexiom.com))
- Google Cloud credentials: `gcloud auth application-default login`

### 1. Clone and install

```bash
git clone https://github.com/synexiom-labs/cortexiom-orchestrator.git
cd cortexiom-orchestrator
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure environment

```bash
cp .env.example .env
```

Edit `.env`:

```env
GCP_PROJECT_ID=cortexiom-orchestrator
GCP_REGION=us-central1
GCS_BUCKET_NAME=cortexiom-orchestrator-data

# Get your key at developers.cortexiom.com
CORTEXIOM_API_KEY=cx_live_your_key_here
CORTEXIOM_API_URL=https://api.cortexiom.com/v1/encounter

# For Gemini — use either:
GOOGLE_API_KEY=your_google_ai_studio_key   # or set via gcloud ADC
```

### 3. Upload data to GCS (optional — local file fallback works without this)

```bash
python scripts/setup_gcs.py
```

### 4. Run the demo

```bash
streamlit run frontend/app.py
```

Open `http://localhost:8501` — select a test case, click **▶ Run Comparison**.

### 5. Run via ADK CLI

```bash
adk run .
# or open the ADK developer UI:
adk web .
```

---

## Deploy to Cloud Run

```bash
# Build and push container
gcloud builds submit --tag gcr.io/cortexiom-orchestrator/cortexiom-orchestrator .

# Set secrets
gcloud secrets create cortexiom-api-key --data-file=- <<< "$CORTEXIOM_API_KEY"
gcloud secrets create google-api-key --data-file=- <<< "$GOOGLE_API_KEY"

# Deploy
gcloud run services replace deployment/cloudrun.yaml --region=us-central1

# Grant public access
gcloud run services add-iam-policy-binding cortexiom-orchestrator \
  --region=us-central1 \
  --member="allUsers" \
  --role="roles/run.invoker"
```

---

## Project Structure

```
cortexiom-orchestrator/
├── agent.py                        ← ADK root agent entry point
├── requirements.txt
├── .env.example
│
├── agents/
│   ├── coordinator.py              ← ADK LlmAgent — orchestrates sub-agents
│   ├── document_parser.py          ← ADK LlmAgent — extracts regulation rules
│   ├── evidence_gatherer.py        ← ADK LlmAgent — searches knowledge base
│   └── recommendation_drafter.py  ← ADK LlmAgent — synthesizes recommendation
│
├── cortexiom/
│   ├── schemas.py                  ← Pydantic models
│   └── reasoner.py                 ← cortexiom_reason() — API call wrapper
│
├── workflow/
│   ├── baseline.py                 ← 3-stage pipeline, no supervision
│   └── supervised.py               ← same pipeline + Cortexiom at 3 checkpoints
│
├── test_cases/
│   └── cases.py                    ← 5 test cases with expected outcomes
│
├── data/
│   ├── regulations/                ← 5 synthetic regulation documents
│   ├── knowledge_base/             ← 5 synthetic org knowledge base documents
│   └── adverse_flags/              ← restricted flags (outside EvidenceGatherer scope)
│
├── frontend/
│   └── app.py                      ← Streamlit side-by-side demo
│
├── scripts/
│   └── setup_gcs.py                ← upload data to GCS + configure Vertex AI Search
│
├── deployment/
│   ├── Dockerfile
│   └── cloudrun.yaml
│
└── docs/
    └── architecture.md
```

---

## How Cortexiom fits the challenge requirements

| Challenge Requirement | How we meet it |
|---|---|
| Multi-agent system | DocumentParser + EvidenceGatherer + RecommendationDrafter, coordinated by an ADK LlmAgent |
| Google ADK 2.0 | All agents defined as `LlmAgent`; coordinator uses `AgentTool`; `root_agent` supports `adk run .` |
| Gemini model | `gemini-2.5-flash` used for all agent calls |
| Vertex AI platform | ADK agents run on Vertex AI; optional Vertex AI Search for semantic retrieval |
| Third-party AI service | Cortexiom API — a reasoning service with confidence scores, depth indicators, and encrypted session state |
| Clear value demonstration | Side-by-side comparison shows exactly what the supervised workflow catches that baseline misses |

---

## About Cortexiom

Cortexiom is a reasoning API built on the Wisdom Architecture — a multi-step reasoning framework designed for decisions where AI getting it wrong is a product failure. It applies Observer → Hypothesis → Contradiction → Calibration → Reflection reasoning to any prompt, returning calibrated responses with confidence scores and session continuity via encrypted state tokens.

Built by [Synexiom Labs](https://synexiomlabs.com) · Cape Breton Island, Nova Scotia, Canada

---

*All regulatory documents and organizational knowledge base content in `data/` are synthetic and created for demonstration purposes only.*