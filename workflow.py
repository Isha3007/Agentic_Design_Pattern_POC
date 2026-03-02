import asyncio
import json


from agents import (
    planning_agent,
    routing_agent,
    action_agent,
    decision_agent,
    risk_agent,
    documentation_agent,
    summary_agent,
    reflection_agent,
    tool_planner_agent,
    language_detection_agent,
    normalization_agent,
    confluence_formatter_agent
)

from tools import (
    create_jira_ticket,
    create_confluence_page,
    send_slack_message,
    send_teams_message
)


async def run_workflow(transcript, mode, detect_language=True):
    lang_info = "unknown"  

    # =====================================================
    # LANGUAGE DETECTION → NORMALIZATION CHAIN
    # =====================================================

    if detect_language:

        print("\n===== LANGUAGE DETECTION =====")

        lang_info = language_detection_agent(transcript)
        print(lang_info)

        print("\n===== NORMALIZATION =====")

        normalized = normalization_agent(transcript, lang_info)
        print(normalized)

        transcript = normalized

    # =====================================================
    # PLANNING
    # =====================================================

    print("\n===== PLANNING =====")

    plan = planning_agent(transcript, mode)
    print(plan)

    # =====================================================
    # ROUTING
    # =====================================================

    print("\n===== ROUTING =====")

    route = routing_agent(mode)
    print(route)

    try:
        route_data = json.loads(route)
    except:
        route_data = {"pipeline": mode, "tools": []}

    pipeline = route_data.get("pipeline", mode)

    print("\n===== EXECUTION PIPELINE =====")

    # =====================================================
    # SPRINT PIPELINE (PARALLEL AGENTS)
    # =====================================================

    if pipeline == "sprint":

        actions, decisions, risks = await asyncio.gather(
            action_agent(transcript),
            decision_agent(transcript),
            risk_agent(transcript)
        )

        combined = f"""
Actions:
{actions}

Decisions:
{decisions}

Risks:
{risks}
"""

    # =====================================================
    # KNOWLEDGE TRANSFER
    # =====================================================
    elif pipeline == "kt":

        print("\n===== KT CHUNKING =====")

        chunks = chunk_text(transcript)

        docs = []

        for chunk in chunks:
            part = await documentation_agent(chunk)
            docs.append(part)

        merged_doc = "\n\n".join(docs)

        combined = f"""
    Knowledge Transfer Document:

    {merged_doc}
    """

    # =====================================================
    # GENERAL MEETING
    # =====================================================

    else:

        summary = await summary_agent(transcript)

        combined = f"""
Meeting Summary:

{summary}
"""

    # =====================================================
    # REFLECTION
    # =====================================================

    print("\n===== REFLECTION =====")

    improved = reflection_agent(combined)
    print(improved)

    print("\n===== CONFLUENCE FORMAT =====")

    confluence_html = confluence_formatter_agent(
        improved,
        transcript,
        mode,
        lang_info if detect_language else "unknown"
    )
    print("HTML SIZE:", len(confluence_html))  
    # =====================================================
    # TOOL PLANNING
    # =====================================================

    print("\n===== TOOL PLANNING =====")

    tools = tool_planner_agent(improved)
    print("Tools:", tools)


    # =====================================================
    # TOOL EXECUTION
    # =====================================================

    print("\n===== TOOL EXECUTION =====")

    # if "jira" in tools:
    #     create_jira_ticket(improved)

    # if "confluence" in tools:
    #     title = f"Copilot CLI - {mode}"

    #     create_confluence_page(title, confluence_html)
    # Always create Confluence for sprint and kt
    if mode in ["sprint", "kt", "general"]:

        title = f"Copilot KT session - {mode}"

        create_confluence_page(title, confluence_html)

    # if "slack" in tools:
    #     send_slack_message(improved)

    # if "teams" in tools:
    #     send_teams_message(improved)

    return improved

def chunk_text(text, size=4000):
    return [text[i:i + size] for i in range(0, len(text), size)]