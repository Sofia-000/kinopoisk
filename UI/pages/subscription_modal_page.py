"""Subscription modal page object."""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage


class SubscriptionModalPage(BasePage):
    """Subscription modal window."""

    # Locators
    MODAL_WINDOW = (By.CSS_SELECTOR, "[role='dialog'], .modal, [class*='Modal']")
    TRY_FREE_BUTTON = (By.XPATH, "//button[contains(text(), 'Попробовать бесплатно')]")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[data-testid='submit-button']")

    def __init__(self, driver: WebDriver) -> None:
        """Initialize subscription modal page.

        Args:
            driver: WebDriver instance
        """
        super().__init__(driver)

    @allure.step("Wait for subscription modal to open")
    def wait_for_modal_to_open(self) -> None:
        """Wait for subscription modal window to appear."""
        self.wait_for_element_visible(self.TRY_FREE_BUTTON, timeout=10)

    @allure.step("Click 'Попробовать бесплатно' button")
    def click_try_free_button(self) -> None:
        """Click on 'Попробовать бесплатно' button."""
        self.click_element(self.TRY_FREE_BUTTON)

    @allure.step("Check if submit button is visible")
    def is_submit_button_visible(self) -> bool:
        """Check if 'Подключить' submit button is visible.

        Returns:
            True if submit button is visible, False otherwise
        """
        return self.is_element_visible(self.SUBMIT_BUTTON, timeout=10)

    @allure.step("Wait for submit button to appear")
    def wait_for_submit_button(self) -> None:
        """Wait for 'Подключить' submit button to appear."""
        self.wait_for_element_visible(self.SUBMIT_BUTTON, timeout=15)
