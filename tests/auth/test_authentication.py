import allure
import pytest

from src.pages.auth_page import AuthPage
from src.pages.inventory_page import InventoryPage
from src.config.settings import SLOW_TIMEOUT


@allure.feature("Авторизация")
class TestAuthentication:
    @allure.title("Успешный логин (standard_user / secret_sauce)")
    def test_login_success(self, driver, base_url, default_timeout):
        auth = AuthPage(driver)
        inventory = InventoryPage(driver)

        auth.open_auth(base_url, timeout=default_timeout)
        auth.login("standard_user", "secret_sauce", timeout=default_timeout)
        inventory.assert_opened(timeout=default_timeout)

    @allure.title("Логин с неверным паролем")
    def test_login_wrong_password(self, driver, base_url, default_timeout):
        auth = AuthPage(driver)

        auth.open_auth(base_url, timeout=default_timeout)
        auth.login("standard_user", "wrong_pass", timeout=default_timeout)

        auth.assert_error_contains("Username and password do not match", timeout=default_timeout)

        assert "saucedemo.com" in driver.current_url

    @allure.title("Логин заблокированного пользователя (locked_out_user)")
    def test_login_locked_out_user(self, driver, base_url, default_timeout):
        auth = AuthPage(driver)

        auth.open_auth(base_url, timeout=default_timeout)
        auth.login("locked_out_user", "secret_sauce", timeout=default_timeout)

        auth.assert_error_contains("locked out", timeout=default_timeout)
        assert "inventory.html" not in driver.current_url

    @allure.title("Логин с пустыми полями")
    def test_login_empty_fields(self, driver, base_url, default_timeout):
        auth = AuthPage(driver)

        auth.open_auth(base_url, timeout=default_timeout)
        auth.login_empty(timeout=default_timeout)

        auth.assert_error_contains("Username is required", timeout=default_timeout)
        assert "inventory.html" not in driver.current_url

    @allure.title("Логин performance_glitch_user (страница открывается несмотря на задержки)")
    @pytest.mark.slow
    def test_login_performance_glitch_user(self, driver, base_url, default_timeout):
        auth = AuthPage(driver)
        inventory = InventoryPage(driver)

        auth.open_auth(base_url, timeout=default_timeout)
        auth.login("performance_glitch_user", "secret_sauce", timeout=default_timeout)

        inventory.assert_opened(timeout=SLOW_TIMEOUT)
