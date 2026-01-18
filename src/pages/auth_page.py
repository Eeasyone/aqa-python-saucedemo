import allure
from selenium.webdriver.common.by import By

from src.core.base_page import BasePage
from src.utils.waits import wait_visible


class AuthPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    @allure.step("Открыть страницу авторизации")
    def open_auth(self, url: str, timeout: int = 10):
        self.driver.get(url)
        wait_visible(self.driver, self.USERNAME_INPUT, timeout=timeout)

    @allure.step("Авторизоваться пользователем")
    def login(self, username: str, password: str, timeout: int = 10):
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()

    @allure.step("Проверить сообщение об ошибке")
    def assert_error(self, expected_text: str, timeout: int = 10):
        error = wait_visible(self.driver, self.ERROR_MESSAGE, timeout=timeout)
        assert expected_text in error.text, (
            f"Ожидали сообщение '{expected_text}', получили '{error.text}'"
        )
