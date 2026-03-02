import os
from dotenv import load_dotenv

load_dotenv()

AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_EMBEDDING = os.getenv("AZURE_EMBEDDING_DEPLOYMENT")
CONFLUENCE_BASE_URL = os.getenv("BASE_URL_CONF")
CONFLUENCE_EMAIL = "ishita.ramdasi@tomtom.com"
CONFLUENCE_API_TOKEN = os.getenv("CONF_API_TOKEN")
CONFLUENCE_SPACE_KEY = os.getenv("CONF_SPACE_KEY")