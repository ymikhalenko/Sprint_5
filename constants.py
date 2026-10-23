from dotenv import load_dotenv
import os

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
GET_WEB_ELEMENT_TIMEOUT = int(os.getenv("GET_WEB_ELEMENT_TIMEOUT") or '3')
REGISTERED_LOGIN = os.getenv("REGISTERED_LOGIN")
REGISTERED_PASSWORD = os.getenv("REGISTERED_PASSWORD")

REGISTRATION_ERROR_FRAMES_COUNT = 3
CITY = 'Санкт-Петербург'
