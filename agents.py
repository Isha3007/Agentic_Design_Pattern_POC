import json
from openai import AzureOpenAI
from config import AZURE_API_KEY, AZURE_ENDPOINT

client = AzureOpenAI(
    api_key=AZURE_API_KEY,
    azure_endpoint=AZURE_ENDPOINT,
    api_version="2024-08-01-preview"
)


# ---------- BASE LLM ----------
def llm_call(system, user):

    response = client.chat.completions.create(
        model="dep-gpt-4o",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


# =========================================================
# PLANNING AGENT
# =========================================================

def planning_agent(transcript, mode):

    system = """
You are a planning agent.

Convert the goal into execution steps.

Mode meanings:
- sprint → create tasks & actions
- kt → knowledge transfer documentation
- general → meeting summary

Return JSON:
{
  "goal": "",
  "steps": []
}
"""

    user = f"""
Mode: {mode}

Transcript:
{transcript}
"""

    return llm_call(system, user)


# =========================================================
# ROUTING AGENT
# =========================================================

def routing_agent(mode):

    system = """
You are a routing agent.

Map mode to pipeline.

Return JSON:
{
  "pipeline": "",
  "tools": []
}
"""

    user = f"Mode: {mode}"

    return llm_call(system, user)


# =========================================================
# WORKER AGENTS
# =========================================================

async def action_agent(transcript):

    system = "Extract actionable tasks with owners and deadlines."

    return llm_call(system, transcript)


async def decision_agent(transcript):

    system = "Extract decisions made in the meeting."

    return llm_call(system, transcript)


async def risk_agent(transcript):

    system = "Extract risks and blockers."

    return llm_call(system, transcript)


async def documentation_agent(transcript):

    system = "Create structured knowledge transfer documentation."

    return llm_call(system, transcript)


async def summary_agent(transcript):

    system = "Create concise meeting summary."

    return llm_call(system, transcript)


# =========================================================
# REFLECTION AGENT
# =========================================================

def reflection_agent(draft):

    system = """
You are a reflection agent.

Improve reliability and clarity.

Steps:
1. Identify problems
2. Improve structure
3. Return final output
"""

    return llm_call(system, draft)


# =========================================================
# TOOL PLANNER
# =========================================================

def tool_planner_agent(context):

    system = """
Decide tools needed.

Available:
confluence, slack, teams

Return JSON list.
"""

    return llm_call(system, context)

# =========================================================
# LANGUAGE DETECTION AGENT
# =========================================================

def language_detection_agent(transcript):

    system = """
You are a language detection agent.

Detect the language(s) used in the transcript.

Return JSON:
{
  "primary_language": "",
  "other_languages": [],
  "is_mixed": true/false
}
"""

    return llm_call(system, transcript)

# =========================================================
# NORMALIZATION AGENT
# =========================================================

def normalization_agent(transcript, language_info):

    system = """
You are a normalization agent.

Your task:
Convert the transcript into clear professional English.

Use language detection info to guide translation.

Rules:
- Preserve names
- Preserve technical terms
- Preserve deadlines
- Do not remove meaning

Return normalized transcript only.
"""

    user = f"""
Language Info:
{language_info}

Transcript:
{transcript}
"""

    return llm_call(system, user)

# =========================================================
# CONFLUENCE FORMATTER AGENT
# =========================================================
def confluence_formatter_agent(final_output, transcript, mode, language_info):

    system = f"""
You are a Confluence documentation specialist.

Format content based on meeting mode.

Mode = {mode}

Rules:

If mode = sprint:
    Include:
    - Metadata
    - Actions
    - Decisions
    - Risks
    - Insights

If mode = kt:
    Create detailed knowledge document with:

    - Overview
    - Topics Covered
    - Detailed Explanations
    - Technical Notes
    - Examples
    - Key Insights
    - Best Practices
    - Additional Notes

If mode = general:
    Include:
    - Summary
    - Key Points
    - Decisions
    - Follow Ups

Return clean HTML only.
"""

    user = f"""
Language Info:
{language_info}

Content:
{final_output}

Transcript:
{transcript}
"""

    return llm_call(system, user)