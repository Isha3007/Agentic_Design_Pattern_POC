# def create_jira_ticket(data):
#     print("Creating Jira Ticket...")
#     return "JIRA-123"


import requests
from config import CONFLUENCE_BASE_URL, CONFLUENCE_EMAIL, CONFLUENCE_API_TOKEN, CONFLUENCE_SPACE_KEY


def create_confluence_page(title, html_content):

    url = f"{CONFLUENCE_BASE_URL}/wiki/rest/api/content"

    headers = {
        "Content-Type": "application/json"
    }

    auth = (CONFLUENCE_EMAIL, CONFLUENCE_API_TOKEN)

    data = {
        "type": "page",
        "title": title,
        "space": {
            "key": CONFLUENCE_SPACE_KEY
        },
        "body": {
            "storage": {
                "value": html_content,
                "representation": "storage"
            }
        }
    }

    response = requests.post(url, json=data, headers=headers, auth=auth)

    if response.status_code == 200 or response.status_code == 201:
        print("Confluence page created")
    else:
        print("Confluence error:", response.text)


# def send_slack_message(data):
#     print("Sending Slack Message...")


# def send_teams_message(data):
#     print("Sending Teams Message...")