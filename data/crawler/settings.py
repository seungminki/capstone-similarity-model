import os
from dotenv import load_dotenv

load_dotenv()

EVERYTIME_ID = os.getenv("EVERYTIME_ID")
EVERYTIME_PASSWORD = os.getenv("EVERYTIME_PASSWORD")

EVERYTIME_URL = os.getenv("EVERYTIME_URL")

CHROMEDRIVER_PATH = os.getenv("DRIVER_PATH")
