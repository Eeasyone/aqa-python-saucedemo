from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_url_contains(driver, text: str, timeout: int = 10):
    WebDriverWait(driver, timeout).until(EC.url_contains(text))


def wait_visible(driver, locator, timeout: int = 10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))


def wait_clickable(driver, locator, timeout: int = 10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
