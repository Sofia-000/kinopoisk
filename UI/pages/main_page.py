import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from config import config


class MainPage(BasePage):
    MEDIA_LINK = (By.CSS_SELECTOR, "a[href='/media/']")
    LOGO = (By.CSS_SELECTOR, "[data-tid='kinopoisk-logo']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='kp_query']")
    TOP_250_LINK = (By.CSS_SELECTOR, "a[href='/lists/movies/top250/']")
    SERIES_LINK = (By.CSS_SELECTOR, "a[href='/series/']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[data-tid='CloseButton']")
    SUGGEST_CONTAINER = (By.CSS_SELECTOR, ".kinopoisk-header-suggest__groups-container")
    FIRST_SUGGEST_LINK = (By.CSS_SELECTOR, ".kinopoisk-header-suggest-item a")
    CINEMA_TICKETS_LINK = (By.CSS_SELECTOR, "a.kinopoisk-header-featured-menu__item[href*='/lists/movies/movies-in-cinema/']")
    ONLINE_CINEMA_LINK = (By.CSS_SELECTOR, "a[href='https://hd.kinopoisk.ru/']")
    EXPAND_SUBSCRIPTION_BUTTON = (By.CSS_SELECTOR, "button.style_buttonSecondary__MO6v_")
    TRY_FREE_BUTTON = (By.CSS_SELECTOR, "button.style_button__Awsrq.style_buttonSize48__6gVtj.style_buttonPlus__2wkyd.style_buttonLight__C8cK7")
    CONNECT_BUTTON = (By.CSS_SELECTOR, "button.Button_5-3-1_87b77")


    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.url = config.BASE_URL

    @allure.step("Open main page")
    def open(self) -> None:
        self.open_url(self.url)

    @allure.step("Close modal window if present")
    def close_modal_if_present(self) -> None:
        if self.is_element_visible(self.MODAL_CLOSE_BUTTON, timeout=2):
            self.click_element(self.MODAL_CLOSE_BUTTON)

    @allure.step("Click Media link")
    def click_media_link(self) -> None:
        self.click_element(self.MEDIA_LINK)

    @allure.step("Check if logo is visible")
    def is_logo_visible(self) -> bool:
        return self.is_element_visible(self.LOGO)

    @allure.step("Check if search input is visible")
    def is_search_visible(self) -> bool:
        return self.is_element_visible(self.SEARCH_INPUT)

    @allure.step("Click Top 250 link")
    def click_top_250_link(self) -> None:
        self.click_element(self.TOP_250_LINK)

    @allure.step("Click Series link")
    def click_series_link(self) -> None:
        self.click_element(self.SERIES_LINK)

    @allure.step("Enter search query: {query}")
    def enter_search_query(self, query: str) -> None:
        search_input = self.wait_for_element_clickable(self.SEARCH_INPUT)
        search_input.click()
        search_input.clear()
        search_input.send_keys(query)

    @allure.step("Wait for search suggestions to appear")
    def wait_for_search_suggestions(self) -> None:
        self.wait_for_element_visible(self.SUGGEST_CONTAINER)

    @allure.step("Check if search suggestions are visible")
    def are_search_suggestions_visible(self) -> bool:
        return self.is_element_visible(self.SUGGEST_CONTAINER)

    @allure.step("Click first search suggestion")
    def click_first_suggestion(self) -> None:
        self.click_element(self.FIRST_SUGGEST_LINK)

    @allure.step("Click cinema tickets link")
    def click_cinema_tickets_link(self) -> None:
        self.click_element(self.CINEMA_TICKETS_LINK)

    @allure.step("Click online cinema link")
    def click_online_cinema_link(self) -> None:
        self.click_element(self.ONLINE_CINEMA_LINK)

    @allure.step("Click expand subscription button")
    def click_expand_subscription_button(self) -> None:
        self.click_element(self.EXPAND_SUBSCRIPTION_BUTTON)
        
    @allure.step("Click 'Try free' button in modal")
    def click_try_free_button(self) -> None:
        self.click_element(self.TRY_FREE_BUTTON)
        
    @allure.step("Check if connect button is visible")
    def is_connect_button_visible(self) -> bool:
        return self.is_element_visible(self.CONNECT_BUTTON, timeout=10)