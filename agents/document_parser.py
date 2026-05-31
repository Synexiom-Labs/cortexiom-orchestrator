"""
ADK Agent — DocumentParser

Reads a regulation document and extracts structured compliance rules:
applicable entities, requirements, thresholds, effective dates, penalties.
"""
from pathlib import Path

from google.adk.agents import LlmAgent

DATA_DIR = Path(__file__).parent.parent / "data"


def read_regulation(file_name: str) -> str:
    """
    Read a regulation document from data/regulations/.

    Args:
        file_name: filename (e.g. 'edd_regulation.md')

    Returns:
        Full text of the regulation document.
    """
    path = DATA_DIR / "regulations" / file_name
    if not path.exists():
        available = [f.name for f in (DATA_DIR / "regulations").glob("*.md")]
        return (
            f"File '{file_name}' not found. "
            f"Available regulations: {', '.join(available)}"
        )
    return path.read_text(encoding="utf-8")


def list_regulations() -> str:
    """
    List all available regulation documents.

    Returns:
        Comma-separated list of regulation filenames.
    """
    reg_dir = DATA_DIR / "regulations"
    files = [f.name for f in reg_dir.glob("*.md")]
    return ", ".join(files) if files else "No regulation documents found."


document_parser = LlmAgent(
    name="document_parser",
    model="gemini-2.5-flash",
    description=(
        "Parses regulation and policy documents, extracting structured compliance rules "
        "including: applicable entities, mandatory requirements, numeric thresholds, "
        "effective dates, and penalties for non-compliance."
    ),
    instruction=(
        "You are a compliance document parser. When given a regulation filename, "
        "use read_regulation to retrieve it, then extract:\n"
        "1. Applicable entities (who must comply)\n"
        "2. Core requirements (what must be done)\n"
        "3. Thresholds and numeric triggers\n"
        "4. Effective dates and deadlines\n"
        "5. Documentation standards\n"
        "6. Penalties for non-compliance\n\n"
        "Return your output as a structured list. Be precise — do not paraphrase "
        "requirements in ways that soften their mandatory nature."
    ),
    tools=[read_regulation, list_regulations],
)