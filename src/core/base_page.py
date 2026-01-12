from src.utils.waits import wait_url_contains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)

    def should_have_url_contains(self, text: str, timeout: int):
        wait_url_contains(self.driver, text, timeout=timeout)
