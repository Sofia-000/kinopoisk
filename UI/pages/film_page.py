import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage


class FilmPage(BasePage):
    FILM_TITLE = (By.CSS_SELECTOR, "h1[itemprop='name']")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    @allure.step("Wait for film page to load")
    def wait_for_film_page_to_load(self) -> None:
        self.wait_for_element_visible(self.FILM_TITLE)

    @allure.step("Get film title")
    def get_film_title(self) -> str:
        return self.get_element_text(self.FILM_TITLE)

    @allure.step("Check if film title is visible")
    def is_film_title_visible(self) -> bool:
        return self.is_element_visible(self.FILM_TITLE)
