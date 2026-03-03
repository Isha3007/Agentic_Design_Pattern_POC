import os
from dotenv import load_dotenv

load_dotenv()

AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")

CONFLUENCE_BASE_URL = os.getenv("BASE_URL_CONF")
CONFLUENCE_EMAIL = os.getenv("CONF_EMAIL")
CONFLUENCE_API_TOKEN = os.getenv("CONF_API_TOKEN")
CONFLUENCE_SPACE_KEY = os.getenv("CONF_SPACE_KEY")