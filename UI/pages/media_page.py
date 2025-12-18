"""Media page object for Kinopoisk."""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage


class MediaPage(BasePage):
    ARTICLES_GRID = (By.CSS_SELECTOR, ".posts-grid")
    FIRST_ARTICLE_CARD = (By.CSS_SELECTOR, ".post-feature-card:first-of-type")
    FIRST_ARTICLE_LINK = (By.CSS_SELECTOR, ".post-feature-card:first-of-type .post-feature-card__link")
    ARTICLE_CARDS = (By.CSS_SELECTOR, ".post-feature-card")
    ARTICLE_TITLE = (By.CSS_SELECTOR, ".post-feature-card__title")

    def __init__(self, driver: WebDriver) -> None:
       
        super().__init__(driver)

    @allure.step("Wait for articles to load")
    def wait_for_articles_to_load(self) -> None:
        self.wait_for_element_visible(self.ARTICLES_GRID)

    @allure.step("Click first article")
    def click_first_article(self) -> None:
        self.wait_for_element_clickable(self.FIRST_ARTICLE_LINK)
        self.click_element(self.FIRST_ARTICLE_LINK)

    @allure.step("Get first article title")
    def get_first_article_title(self) -> str:
        first_card = self.wait_for_element_visible(self.FIRST_ARTICLE_CARD)
        title_element = first_card.find_element(By.CSS_SELECTOR, ".post-feature-card__title")
        return title_element.text

    @allure.step("Get articles count")
    def get_articles_count(self) -> int:
        articles = self.find_elements(self.ARTICLE_CARDS)
        return len(articles)

    @allure.step("Check if articles are visible")
    def are_articles_visible(self) -> bool:
        return self.is_element_visible(self.FIRST_ARTICLE_CARD)
