from dotenv import load_dotenv
import os

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
GET_WEB_ELEMENT_TIMEOUT = int(os.getenv("GET_WEB_ELEMENT_TIMEOUT") or '3')

REGISTERED_LOGIN = 'test@gmail.com'
REGISTERED_PASSWORD = '123qweASD'
