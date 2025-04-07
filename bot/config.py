import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
DJANGO_API_URL = "http://127.0.0.1:8000/api/bot/"
API_URL = "http://127.0.0.1:8000"