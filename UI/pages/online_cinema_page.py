import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage


class OnlineCinemaPage(BasePage):
    PAGE_CONTENT = (By.CSS_SELECTOR, "body")
    USER_AVATAR_LINK = (By.CSS_SELECTOR, "a[href='/']")
    FIRST_FILM_CARD = (By.CSS_SELECTOR, ".CarouselItem_root__WOZNE:first-of-type a[href*='/film/']")
    FILM_CARDS = (By.CSS_SELECTOR, ".CarouselItem_root__WOZNE")
    WATCH_BUTTON = (By.CSS_SELECTOR, "button[name='Watch']")
    FILM_SLIDER = (By.CSS_SELECTOR, "[data-tid='Selections']")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    @allure.step("Wait for online cinema page to load")
    def wait_for_page_to_load(self) -> None:
        self.wait_for_element_visible(self.PAGE_CONTENT)

    @allure.step("Check if page URL contains hd.kinopoisk.ru")
    def is_on_online_cinema_page(self) -> bool:
        current_url = self.get_current_url()
        return "hd.kinopoisk.ru" in current_url

    @allure.step("Click user avatar to go to profile")
    def click_user_avatar(self) -> None:
        self.click_element(self.USER_AVATAR_LINK)

    @allure.step("Wait for film cards to load")
    def wait_for_film_cards(self) -> None:
        self.wait_for_element_visible(self.FILM_CARDS)

    @allure.step("Click first film card")
    def click_first_film_card(self) -> None:
        self.click_element(self.FIRST_FILM_CARD)

    @allure.step("Wait for film slider to expand")
    def wait_for_film_slider(self) -> None:
        self.wait_for_element_visible(self.FILM_SLIDER)

    @allure.step("Click watch button")
    def click_watch_button(self) -> None:
        self.click_element(self.WATCH_BUTTON)
