import asyncio
from workflow import run_workflow


if __name__ == "__main__":

    transcript = """
"""
    mode = "kt"   # sprint | kt | general
    detect_language=True

    mode = "kt"  # sprint | kt | general

    result = asyncio.run(
        run_workflow(transcript, session_mode="kt")
    )

    print("\n========== FINAL OUTPUT ==========\n")
    print(result)