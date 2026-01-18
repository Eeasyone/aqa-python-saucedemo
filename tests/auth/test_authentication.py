import allure
import pytest

from src.pages.auth_page import AuthPage
from src.pages.inventory_page import InventoryPage
from src.config.settings import SLOW_TIMEOUT

from src.test_data.users import (
    STANDARD_USER,
    LOCKED_OUT_USER,
    PERFORMANCE_GLITCH_USER,
    INVALID_PASSWORD_USER,
)
from src.test_data import messages


@allure.feature("Авторизация")
class TestAuthentication:
    @allure.title("Успешный логин (standard_user / secret_sauce)")
    def test_login_success(self, driver, base_url, default_timeout):
        auth = AuthPage(driver)
        inventory = InventoryPage(driver)

        auth.open_auth(base_url, timeout=default_timeout)
        auth.login(
            STANDARD_USER.username,
            STANDARD_USER.password,
            timeout=default_timeout,
        )

        inventory.assert_opened(timeout=default_timeout)

    @allure.title("Логин с неверным паролем")
    def test_login_wrong_password(self, driver, base_url, default_timeout):
        auth = AuthPage(driver)

        auth.open_auth(base_url, timeout=default_timeout)
        auth.login(
            INVALID_PASSWORD_USER.username,
            INVALID_PASSWORD_USER.password,
            timeout=default_timeout,
        )

        auth.assert_error(messages.INVALID_CREDENTIALS, timeout=default_timeout)
        assert "inventory.html" not in driver.current_url

    @allure.title("Логин заблокированного пользователя (locked_out_user)")
    def test_login_locked_out_user(self, driver, base_url, default_timeout):
        auth = AuthPage(driver)

        auth.open_auth(base_url, timeout=default_timeout)
        auth.login(
            LOCKED_OUT_USER.username,
            LOCKED_OUT_USER.password,
            timeout=default_timeout,
        )

        auth.assert_error(messages.LOCKED_OUT, timeout=default_timeout)
        assert "inventory.html" not in driver.current_url

    @allure.title("Логин с пустыми полями")
    def test_login_empty_fields(self, driver, base_url, default_timeout):
        auth = AuthPage(driver)

        auth.open_auth(base_url, timeout=default_timeout)
        auth.login("", "", timeout=default_timeout)

        auth.assert_error(messages.USERNAME_REQUIRED, timeout=default_timeout)
        assert "inventory.html" not in driver.current_url

    @allure.title("Логин performance_glitch_user (страница открывается несмотря на задержки)")
    @pytest.mark.slow
    def test_login_performance_glitch_user(self, driver, base_url, default_timeout):
        auth = AuthPage(driver)
        inventory = InventoryPage(driver)

        auth.open_auth(base_url, timeout=default_timeout)
        auth.login(
            PERFORMANCE_GLITCH_USER.username,
            PERFORMANCE_GLITCH_USER.password,
            timeout=default_timeout,
        )

        inventory.assert_opened(timeout=SLOW_TIMEOUT)
