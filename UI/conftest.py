"""Pytest configuration and fixtures."""
import os
import sys
import json
import time
import pytest
import allure
from typing import Generator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from config import config

# Добавляем корневую директорию в sys.path для импорта utils
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Импортируем API клиент
from utils.api_client import PoiskKinoAPIClient


def pytest_configure(config):
    """
    Конфигурация pytest с регистрацией маркеров.

    Args:
        config: Объект конфигурации pytest
    """
    config.addinivalue_line(
        "markers", "api: mark test as API test"
    )
    config.addinivalue_line(
        "markers", "ui: mark test as UI test"
    )


@pytest.fixture(scope="function")
def driver() -> Generator[WebDriver, None, None]:
    """Create and configure WebDriver instance.

    Yields:
        WebDriver instance
    """
    with allure.step("Initialize browser"):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        if config.HEADLESS:
            options.add_argument("--headless")

        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(config.IMPLICIT_WAIT)
        browser.maximize_window()

        # Load cookies if available
        cookies_file = os.path.join(os.path.dirname(__file__), "cookies.json")
        if os.path.exists(cookies_file):
            # Need to open a page first before adding cookies
            browser.get(config.BASE_URL)
            with open(cookies_file, 'r', encoding='utf-8') as f:
                cookies = json.load(f)
            for cookie in cookies:
                try:
                    browser.add_cookie(cookie)
                except Exception:
                    # Skip cookies that can't be added
                    pass
            # Refresh page to apply cookies
            browser.refresh()
            # Wait for page to load after applying cookies
            time.sleep(2)

    yield browser

    with allure.step("Close browser"):
        browser.quit()


@pytest.fixture(scope="function")
def api_client() -> Generator[PoiskKinoAPIClient, None, None]:
    """
    Фикстура для создания API клиента.

    Yields:
        PoiskKinoAPIClient: Экземпляр API клиента
    """
    client = PoiskKinoAPIClient()
    yield client
    client.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Pytest hook to capture screenshots on test failure.

    Args:
        item: Test item
        call: Test call info
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if "driver" in item.funcargs:
            driver = item.funcargs["driver"]
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception:
                pass