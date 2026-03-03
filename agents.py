import json
from openai import AzureOpenAI
from config import AZURE_API_KEY, AZURE_ENDPOINT

client = AzureOpenAI(
    api_key=AZURE_API_KEY,
    azure_endpoint=AZURE_ENDPOINT,
    api_version="2024-08-01-preview"
)


# =========================================================
# BASE LLM CALL
# =========================================================

def llm_call(system: str, user: str):
    response = client.chat.completions.create(
        model="dep-gpt-4o",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ],
        temperature=0.1  # deterministic
    )
    return response.choices[0].message.content


# =========================================================
# 1️⃣ LANGUAGE AGENT
# =========================================================

def language_detection_agent(transcript: str):

    system = """
You are a Language Intelligence Agent.

ROLE BOUNDARY:
You ONLY detect language characteristics.
You MUST NOT summarize, normalize, interpret goals, or restructure content.

TASK:
1. Detect primary language.
2. Detect secondary languages if present.
3. Determine if transcript is mixed-language.
4. Provide confidence score.

STRICT OUTPUT FORMAT (JSON ONLY):

{
  "primary_language": "",
  "secondary_languages": [],
  "is_mixed": true/false,
  "confidence": 0.0-1.0
}

CONSTRAINTS:
- Do not hallucinate languages.
- If unsure, lower confidence.
- No commentary outside JSON.
"""

    return llm_call(system, transcript)


def normalization_agent(transcript: str, language_info: str):

    system = """
You are a Transcript Normalization Agent.

ROLE:
Convert transcript into professional English while preserving semantic fidelity.

YOU MUST:
- Preserve technical terms
- Preserve names
- Preserve deadlines
- Preserve meaning exactly

YOU MUST NOT:
- Summarize
- Remove content
- Add new information
- Interpret intent beyond transcript

If transcript already English:
Return cleaned version only.

Return ONLY normalized transcript.
No JSON.
No commentary.
"""

    user = f"""
Language Info:
{language_info}

Transcript:
{transcript}
"""

    return llm_call(system, user)


# =========================================================
# 2️⃣ PLANNER AGENT
# =========================================================

def planning_agent(transcript: str, session_mode: str):

    system = """
You are a Strategic Planning Agent in a multi-agent LLM orchestration system.

ROLE BOUNDARY:
You DO NOT execute.
You DO NOT summarize.
You DO NOT call tools.
You DO NOT produce documentation.

You ONLY produce a structured execution plan.

TASK:
1. Detect session type (KT or General or Sprint).
2. Identify objective.
3. Decompose into ordered phases.
4. Define dependencies.
5. Identify parallelizable phases.

STRICT OUTPUT FORMAT (JSON ARRAY):

[
  {
    "phase_id": 1,
    "phase_name": "",
    "objective": "",
    "expected_output": "",
    "depends_on": [],
    "can_run_parallel": true/false
  }
]

CONSTRAINTS:
- No cyclic dependencies.
- Sequential phase_id.
- No vague phase names.
- Do not hallucinate goals.
- No commentary outside JSON.
"""

    user = f"""
Session Mode Hint: {session_mode}

Normalized Transcript:
{transcript}
"""

    return llm_call(system, user)


# =========================================================
# 3️⃣ ROUTER AGENT
# =========================================================

def router_agent(plan_json: str):

    system = """
You are a Routing Agent.

ROLE:
Map planner phases to execution agents and validate integrity.

AVAILABLE AGENTS:
- summary_agent
- action_agent
- decision_agent
- risk_agent
- documentation_agent

TASK:
1. Validate phase structure.
2. Reject ambiguous phase names.
3. Ensure dependencies reference valid phase_id.
4. Return routing map.

STRICT OUTPUT FORMAT:

{
  "status": "valid" | "invalid",
  "routing_map": [
    {
      "phase_id": 1,
      "agent": ""
    }
  ],
  "error": ""
}

If invalid:
Set status = "invalid" and explain in error.

No commentary outside JSON.
"""

    return llm_call(system, plan_json)


# =========================================================
# 4️⃣ EXECUTION AGENTS
# =========================================================

async def summary_agent(transcript: str):
    system = """
You are a Summary Agent.

Produce concise structured meeting summary.

DO NOT:
- Plan
- Reflect
- Call tools

Return structured markdown summary.
"""
    return llm_call(system, transcript)


async def action_agent(transcript: str):
    return llm_call(
        "Extract structured action items with owners and deadlines.",
        transcript
    )


async def decision_agent(transcript: str):
    return llm_call(
        "Extract structured decisions made during the meeting.",
        transcript
    )


async def risk_agent(transcript: str):
    return llm_call(
        "Extract structured risks and blockers mentioned.",
        transcript
    )


async def documentation_agent(transcript: str):
    system = """
You are a Knowledge Documentation Agent.

Generate structured KT document:

# Overview
# Topics Covered
# Detailed Explanation
# Technical Notes
# Best Practices
# Risks
# Additional Notes

DO NOT:
- Score quality
- Reflect
- Call tools
"""
    return llm_call(system, transcript)


# =========================================================
# 5️⃣ REFLECTION AGENT
# =========================================================

def reflection_agent(context_json: str):

    system = """
You are a Reflection & Evaluation Agent.

TASK:
Compare output vs meeting goal.

Score:
0-100 satisfaction.

Penalize:
- Missing depth
- Vague explanations
- Missing technical clarity

STRICT OUTPUT FORMAT:

{
  "goal_detected": "",
  "goal_satisfaction_score": 0-100,
  "coverage_analysis": "",
  "missing_topics": [],
  "improvement_suggestions": [],
  "confidence": 0.0-1.0
}

No commentary outside JSON.
"""

    return llm_call(system, context_json)


# =========================================================
# 6️⃣ TOOL AGENT
# =========================================================

def tool_planner_agent(context_json: str):

    system = """
You are a Tool Decision Agent.

AVAILABLE TOOLS:
- create_confluence
- send_slack_message
- none

You MUST:
- Only choose from allowed list.
- Justify decision.
- Provide confidence score.

STRICT OUTPUT FORMAT:

{
  "tool": "create_confluence" | "send_slack_message" | "none",
  "reason": "",
  "confidence": 0.0-1.0,
  "payload": {}
}

No commentary outside JSON.
"""

    return llm_call(system, context_json)