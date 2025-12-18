import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage


class CinemaListPage(BasePage):
    BUY_TICKETS_BUTTON = (By.CSS_SELECTOR, "a[href*='/film/'][href*='/afisha/']")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    @allure.step("Wait for cinema list page to load")
    def wait_for_page_to_load(self) -> None:
        self.wait_for_element_visible(self.BUY_TICKETS_BUTTON)

    @allure.step("Click first buy tickets button")
    def click_first_buy_tickets_button(self) -> None:
        self.click_element(self.BUY_TICKETS_BUTTON)
