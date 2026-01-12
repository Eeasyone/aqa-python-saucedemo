import allure
from selenium.webdriver.common.by import By

from src.core.base_page import BasePage
from src.utils.waits import wait_visible, wait_clickable


class AuthPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "[data-test='username']")
    PASSWORD = (By.CSS_SELECTOR, "[data-test='password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "[data-test='login-button']")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    @allure.step("Открыть страницу авторизации")
    def open_auth(self, base_url: str, timeout: int = 10):
        self.open(base_url)
        wait_visible(self.driver, self.USERNAME, timeout=timeout)
        wait_visible(self.driver, self.PASSWORD, timeout=timeout)
        wait_visible(self.driver, self.LOGIN_BTN, timeout=timeout)

    @allure.step("Авторизоваться пользователем {username}")
    def login(self, username: str, password: str, timeout: int = 10):
        user = wait_visible(self.driver, self.USERNAME, timeout=timeout)
        pwd = wait_visible(self.driver, self.PASSWORD, timeout=timeout)

        user.clear()
        pwd.clear()

        user.send_keys(username)
        pwd.send_keys(password)

        wait_clickable(self.driver, self.LOGIN_BTN, timeout=timeout).click()

    @allure.step("Нажать Login с пустыми полями")
    def login_empty(self, timeout: int = 10):
        wait_clickable(self.driver, self.LOGIN_BTN, timeout=timeout).click()

    @allure.step("Проверить ошибку содержит: {text_part}")
    def assert_error_contains(self, text_part: str, timeout: int = 10):
        err = wait_visible(self.driver, self.ERROR, timeout=timeout)
        assert text_part in err.text, f"Ожидали текст '{text_part}', получили '{err.text}'"
