import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage


class PlayerPage(BasePage):
    VIDEO_PLAYER = (By.CSS_SELECTOR, "video")
    PLAYER_CONTAINER = (By.CSS_SELECTOR, "[class*='player'], [class*='Player']")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    @allure.step("Wait for video player to load")
    def wait_for_player_to_load(self) -> None:
        self.wait_for_element_visible(self.VIDEO_PLAYER, timeout=20)

    @allure.step("Check if video player is visible")
    def is_player_visible(self) -> bool:
        return self.is_element_visible(self.VIDEO_PLAYER, timeout=10)

    @allure.step("Check if video is playing")
    def is_video_playing(self) -> bool:
        try:
            video_element = self.find_element(self.VIDEO_PLAYER)

            initial_time = self.driver.execute_script("return arguments[0].currentTime;", video_element)

            time.sleep(2)

            current_time = self.driver.execute_script("return arguments[0].currentTime;", video_element)

            return current_time > initial_time
        except Exception:
            return False

    @allure.step("Get video current time")
    def get_video_current_time(self) -> float:
        video_element = self.find_element(self.VIDEO_PLAYER)
        return self.driver.execute_script("return arguments[0].currentTime;", video_element)

    @allure.step("Check if video is paused")
    def is_video_paused(self) -> bool:
        video_element = self.find_element(self.VIDEO_PLAYER)
        return self.driver.execute_script("return arguments[0].paused;", video_element)
