import requests
from config import (
    CONFLUENCE_BASE_URL,
    CONFLUENCE_EMAIL,
    CONFLUENCE_API_TOKEN,
    CONFLUENCE_SPACE_KEY
)


def create_confluence_page(title, html_content):

    url = f"{CONFLUENCE_BASE_URL}/wiki/rest/api/content"

    data = {
        "type": "page",
        "title": title,
        "space": {"key": CONFLUENCE_SPACE_KEY},
        "body": {
            "storage": {
                "value": html_content,
                "representation": "storage"
            }
        }
    }

    response = requests.post(
        url,
        json=data,
        headers={"Content-Type": "application/json"},
        auth=(CONFLUENCE_EMAIL, CONFLUENCE_API_TOKEN)
    )

    if response.status_code in [200, 201]:
        page_data = response.json()
        page_id = page_data.get("id")
        page_link = f"{CONFLUENCE_BASE_URL}/wiki/pages/{page_id}"
        print("✅ Confluence page created:", page_link)
        return page_link
    else:
        print("❌ Confluence error:", response.text)
        return None


def send_slack_message(message: str):
    # Replace with real webhook if needed
    print("📩 Slack message sent:")
    print(message)