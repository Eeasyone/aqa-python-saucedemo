import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")

HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10"))
SLOW_TIMEOUT = int(os.getenv("SLOW_TIMEOUT", "20"))
