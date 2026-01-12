import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.config.settings import HEADLESS


def create_driver() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/google-chrome"

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1280,720")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if os.path.exists("/.dockerenv"):
        service = Service(executable_path="/usr/bin/chromedriver")
    else:
        service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(0)
    return driver
