from typing import Optional
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import config


class BasePage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, config.EXPLICIT_WAIT)

    @allure.step("Open URL: {url}")
    def open_url(self, url: str) -> None:
        self.driver.get(url)

    @allure.step("Find element: {locator}")
    def find_element(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    @allure.step("Find elements: {locator}")
    def find_elements(self, locator: tuple) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    @allure.step("Wait for element to be visible: {locator}")
    def wait_for_element_visible(self, locator: tuple, timeout: Optional[int] = None) -> WebElement:
        wait_time = timeout if timeout else config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Wait for element to be clickable: {locator}")
    def wait_for_element_clickable(self, locator: tuple, timeout: Optional[int] = None) -> WebElement:
        wait_time = timeout if timeout else config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Click element: {locator}")
    def click_element(self, locator: tuple) -> None:
        element = self.wait_for_element_clickable(locator)
        element.click()

    @allure.step("Get element text: {locator}")
    def get_element_text(self, locator: tuple) -> str:
        element = self.wait_for_element_visible(locator)
        return element.text

    @allure.step("Check if element is visible: {locator}")
    def is_element_visible(self, locator: tuple, timeout: int = 3) -> bool:
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Get current URL")
    def get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Get page title")
    def get_page_title(self) -> str:
        return self.driver.title
