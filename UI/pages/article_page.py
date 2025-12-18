import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage


class ArticlePage(BasePage):
    ARTICLE_TITLE = (By.CSS_SELECTOR, ".media-article__title span[itemprop='headline']")
    ARTICLE_TITLE_CONTAINER = (By.CSS_SELECTOR, ".media-article__title-container")
    ARTICLE_CONTENT = (By.CSS_SELECTOR, ".media-article__content")
    ARTICLE_DATE = (By.CSS_SELECTOR, "time[itemprop='datePublished']")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    @allure.step("Wait for article to load")
    def wait_for_article_to_load(self) -> None:
        self.wait_for_element_visible(self.ARTICLE_TITLE)

    @allure.step("Get article title")
    def get_article_title(self) -> str:
        return self.get_element_text(self.ARTICLE_TITLE)

    @allure.step("Check if article title is visible")
    def is_article_title_visible(self) -> bool:
        return self.is_element_visible(self.ARTICLE_TITLE)

    @allure.step("Check if article content is visible")
    def is_article_content_visible(self) -> bool:
        return self.is_element_visible(self.ARTICLE_CONTENT)

    @allure.step("Get article publication date")
    def get_article_date(self) -> str:
        return self.get_element_text(self.ARTICLE_DATE)
