import allure
from selenium.webdriver.common.by import By

from src.core.base_page import BasePage
from src.utils.waits import wait_visible, wait_url_contains


class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".title")
    INVENTORY_LIST = (By.CSS_SELECTOR, ".inventory_list")
    MENU_BTN = (By.ID, "react-burger-menu-btn")

    @allure.step("Проверить что открылась Inventory страница")
    def assert_opened(self, timeout: int = 10):
        wait_url_contains(self.driver, "inventory.html", timeout=timeout)

        title = wait_visible(self.driver, self.TITLE, timeout=timeout)
        assert title.text == "Products", f"Ожидали заголовок 'Products', получили '{title.text}'"

        wait_visible(self.driver, self.INVENTORY_LIST, timeout=timeout)
        wait_visible(self.driver, self.MENU_BTN, timeout=timeout)
