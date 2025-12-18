"""Sessions page object for Kinopoisk."""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage


class SessionsPage(BasePage):
    SCHEDULE_ITEM = (By.CSS_SELECTOR, ".schedule-item")
    FIRST_SESSION_BUTTON = (By.CSS_SELECTOR, ".schedule-item__session-button.js-yaticket-button")
    IFRAME = (By.CSS_SELECTOR, "iframe")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    @allure.step("Wait for sessions page to load")
    def wait_for_page_to_load(self) -> None:
        self.wait_for_element_visible(self.SCHEDULE_ITEM)

    @allure.step("Click first session button")
    def click_first_session_button(self) -> None:
        self.click_element(self.FIRST_SESSION_BUTTON)

    @allure.step("Check if iframe is visible")
    def is_iframe_visible(self) -> bool:
        return self.is_element_visible(self.IFRAME, timeout=5)
