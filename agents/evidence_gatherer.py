"""
ADK Agent — EvidenceGatherer

Searches the knowledge base (data/knowledge_base/) for evidence relevant to
a compliance topic. Does NOT search data/adverse_flags/ — this is an
intentional design constraint that demonstrates the value of Cortexiom
supervision (the supervised workflow catches this gap at the pre_decision
checkpoint).
"""
import os
from pathlib import Path

from google.adk.agents import LlmAgent

DATA_DIR = Path(__file__).parent.parent / "data"
KB_DIR = DATA_DIR / "knowledge_base"


def search_knowledge_base(topic: str) -> str:
    """
    Search the knowledge base for documents relevant to the given compliance topic.
    Returns full content of all matching documents.

    Args:
        topic: compliance topic or keywords to search for (e.g. 'PEP EDD source of funds')

    Returns:
        Concatenated content of matching documents with filename headers.
    """
    results = []
    keywords = [w.lower() for w in topic.split() if len(w) > 3]

    for doc_path in sorted(KB_DIR.glob("*.md")):
        content = doc_path.read_text(encoding="utf-8")
        content_lower = content.lower()
        if any(kw in content_lower for kw in keywords):
            results.append(f"=== {doc_path.name} ===\n{content}")

    if not results:
        return (
            f"No documents found for topic: '{topic}'. "
            f"Available knowledge base files: "
            f"{', '.join(f.name for f in KB_DIR.glob('*.md'))}"
        )

    return "\n\n".join(results)


def get_document(file_name: str) -> str:
    """
    Retrieve a specific knowledge base document by filename.

    Args:
        file_name: exact filename (e.g. 'pep_client_records.md')

    Returns:
        Full document content.
    """
    path = KB_DIR / file_name
    if not path.exists():
        available = [f.name for f in KB_DIR.glob("*.md")]
        return (
            f"File '{file_name}' not found. "
            f"Available files: {', '.join(available)}"
        )
    return path.read_text(encoding="utf-8")


def list_knowledge_base() -> str:
    """
    List all available knowledge base documents.

    Returns:
        Comma-separated list of filenames.
    """
    files = [f.name for f in KB_DIR.glob("*.md")]
    return ", ".join(files) if files else "Knowledge base is empty."


# Optional: Vertex AI Search integration
# If VERTEX_AI_SEARCH_DATA_STORE_ID is set, the agent also has access
# to a richer semantic search via Vertex AI. Falls back to file search if not set.

_vertex_tool = None
_vertex_ds_id = os.environ.get("VERTEX_AI_SEARCH_DATA_STORE_ID", "")
if _vertex_ds_id:
    try:
        from google.adk.tools.vertex_ai_search_tool import VertexAISearchTool

        _vertex_tool = VertexAISearchTool(data_store_id=_vertex_ds_id)
    except Exception:
        pass  # fall back to file-based tools

_tools = [search_knowledge_base, get_document, list_knowledge_base]
if _vertex_tool:
    _tools.append(_vertex_tool)


evidence_gatherer = LlmAgent(
    name="evidence_gatherer",
    model="gemini-2.5-flash",
    description=(
        "Gathers evidence from the organization's internal knowledge base — "
        "current state documents, client registers, operational records, and "
        "internal assessments — relevant to a compliance evaluation request."
    ),
    instruction=(
        "You are a compliance evidence gatherer. Your job is to search the "
        "organization's knowledge base and retrieve all documents relevant to "
        "the compliance topic you are given.\n\n"
        "Instructions:\n"
        "1. Use search_knowledge_base with relevant keywords\n"
        "2. Use get_document to retrieve specific files you identify as important\n"
        "3. Extract and summarize the compliance-relevant facts from each document\n"
        "4. Note any gaps — information that should exist but is missing\n\n"
        "IMPORTANT: Your search is limited to data/knowledge_base/. Do not "
        "attempt to access other directories. Report only what you find."
    ),
    tools=_tools,
)