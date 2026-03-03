import asyncio
import json
from dataclasses import dataclass, field

from agents import (
    language_detection_agent,
    normalization_agent,
    planning_agent,
    router_agent,
    summary_agent,
    action_agent,
    decision_agent,
    risk_agent,
    documentation_agent,
    reflection_agent,
    tool_planner_agent
)

from tools import create_confluence_page, send_slack_message


# =========================================================
# SHARED STATE
# =========================================================

@dataclass
class WorkflowState:
    raw_transcript: str
    detected_language: dict = None
    normalized_transcript: str = None
    session_mode: str = None
    plan: list = field(default_factory=list)
    routing_map: list = field(default_factory=list)
    phase_outputs: dict = field(default_factory=dict)
    reflection_output: dict = None
    tool_decision: dict = None


# =========================================================
# WORKFLOW ENGINE
# =========================================================

async def run_workflow(transcript: str, session_mode: str):

    state = WorkflowState(raw_transcript=transcript,
                          session_mode=session_mode)

    # LANGUAGE DETECTION
    state.detected_language = json.loads(
        language_detection_agent(state.raw_transcript)
    )

    # NORMALIZATION
    state.normalized_transcript = normalization_agent(
        state.raw_transcript,
        json.dumps(state.detected_language)
    )

    # PLANNING
    state.plan = json.loads(
        planning_agent(
            state.normalized_transcript,
            state.session_mode
        )
    )

    # ROUTING
    routing_response = json.loads(
        router_agent(json.dumps(state.plan))
    )

    if routing_response["status"] == "invalid":
        raise Exception(f"Routing error: {routing_response['error']}")

    state.routing_map = routing_response["routing_map"]

    # EXECUTION LOOP
    for route in state.routing_map:

        phase_id = route["phase_id"]
        agent_name = route["agent"]

        transcript_input = state.normalized_transcript

        if agent_name == "summary_agent":
            result = await summary_agent(transcript_input)

        elif agent_name == "action_agent":
            result = await action_agent(transcript_input)

        elif agent_name == "decision_agent":
            result = await decision_agent(transcript_input)

        elif agent_name == "risk_agent":
            result = await risk_agent(transcript_input)

        elif agent_name == "documentation_agent":
            result = await documentation_agent(transcript_input)

        else:
            continue

        state.phase_outputs[f"phase_{phase_id}"] = result

    combined_output = "\n\n".join(state.phase_outputs.values())

    # REFLECTION
    state.reflection_output = json.loads(
        reflection_agent(json.dumps({
            "goal": state.plan,
            "output": combined_output
        }))
    )

    # # TOOL DECISION
    # state.tool_decision = json.loads(
    #     tool_planner_agent(json.dumps({
    #         "session_mode": state.session_mode,
    #         "reflection_score": state.reflection_output["goal_satisfaction_score"]
    #     }))
    # )

    # # TOOL EXECUTION
    # if state.tool_decision["tool"] == "create_confluence":
    #     create_confluence_page(
    #         title=f"{state.session_mode.upper()} Session Documentation",
    #         html_content=combined_output
    # #     )

    # if state.tool_decision["tool"] == "send_slack_message":
    #     send_slack_message(state.tool_decision["payload"])

    # =====================================================
    # DETERMINISTIC TOOL EXECUTION BASED ON MODE
    # =====================================================

    slack_message = ""

    if state.session_mode in ["kt", "sprint"]:

        # Create Confluence Page
        page_link = create_confluence_page(
            title=f"{state.session_mode.upper()} Session Documentation",
            html_content=combined_output
        )

        # Send Slack Message with Link
        if page_link:
            slack_message = f"""
📢 {state.session_mode.upper()} session documentation created.

🔗 Confluence Link:
{page_link}
"""
        else:
            slack_message = f"""
⚠️ {state.session_mode.upper()} session completed but Confluence creation failed.
"""

        send_slack_message(slack_message)

    elif state.session_mode == "general":

        # Send Minutes of Meeting directly in Slack
        slack_message = f"""
📌 Minutes of Meeting (General Session):

{combined_output}
"""
        send_slack_message(slack_message)

    return combined_output