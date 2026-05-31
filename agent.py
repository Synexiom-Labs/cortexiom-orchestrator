"""
Root ADK entry point — allows `adk run .` from the project root.

The `root_agent` variable is the ADK convention for identifying
the top-level agent in a project.

Usage:
    adk run .
    adk web .      (opens the ADK developer UI)
"""
import os
from dotenv import load_dotenv

load_dotenv()

from agents.coordinator import coordinator

# ADK convention: root_agent is discovered by `adk run`
root_agent = coordinator