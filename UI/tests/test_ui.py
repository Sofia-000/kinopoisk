"""UI tests for Kinopoisk website."""
import time
import pytest
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from pages import MainPage, MediaPage, ArticlePage, FilmPage, CinemaListPage, SessionsPage, OnlineCinemaPage, PlayerPage


@allure.story("Article Page")
@allure.title("Test opening article from Media page")
@pytest.mark.ui
def test_open_article_from_media_page(driver: WebDriver) -> None:
    with allure.step("Navigate to Kinopoisk main page"):
        main_page = MainPage(driver)
        main_page.open()

    with allure.step("Close modal window if present"):
        main_page.close_modal_if_present()

    with allure.step("Click Media button"):
        main_page.click_media_link()

    with allure.step("Wait for Media page to load"):
        media_page = MediaPage(driver)
        media_page.wait_for_articles_to_load()

    with allure.step("Get title of first article"):
        expected_title = media_page.get_first_article_title()
        assert expected_title, "First article should have a title"

    with allure.step("Click on first article"):
        media_page.click_first_article()

    with allure.step("Wait for article page to load"):
        article_page = ArticlePage(driver)
        article_page.wait_for_article_to_load()

    with allure.step("Verify article title is visible"):
        assert article_page.is_article_title_visible(), "Article title should be visible"

    with allure.step("Verify article title is not empty"):
        actual_title = article_page.get_article_title()
        assert actual_title, "Article title should not be empty"


@allure.story("Search")
@allure.title("Test film search functionality")
@pytest.mark.ui
def test_search_film(driver: WebDriver) -> None:
    with allure.step("Navigate to Kinopoisk main page"):
        main_page = MainPage(driver)
        main_page.open()

    with allure.step("Close modal window if present"):
        main_page.close_modal_if_present()

    with allure.step("Enter search query 'Побег из Шоушенка'"):
        main_page.enter_search_query("Побег из Шоушенка")

    with allure.step("Wait for search suggestions to appear"):
        main_page.wait_for_search_suggestions()

    with allure.step("Verify search suggestions are visible"):
        assert main_page.are_search_suggestions_visible(), "Search suggestions should be visible"

    with allure.step("Click first search suggestion"):
        main_page.click_first_suggestion()

    with allure.step("Wait for film page to load"):
        film_page = FilmPage(driver)
        film_page.wait_for_film_page_to_load()

    with allure.step("Verify film title is visible"):
        assert film_page.is_film_title_visible(), "Film title should be visible"

    with allure.step("Verify film title is not empty"):
        title = film_page.get_film_title()
        assert title, "Film title should not be empty"


@allure.story("Cinema Tickets")
@allure.title("Test buying cinema tickets flow")
@pytest.mark.ui
def test_buy_cinema_tickets(driver: WebDriver) -> None:
    with allure.step("Navigate to Kinopoisk main page"):
        main_page = MainPage(driver)
        main_page.open()

    with allure.step("Close modal window if present"):
        main_page.close_modal_if_present()

    with allure.step("Click 'Билеты в кино' link"):
        main_page.click_cinema_tickets_link()

    with allure.step("Wait for cinema list page to load"):
        cinema_list_page = CinemaListPage(driver)
        cinema_list_page.wait_for_page_to_load()

    with allure.step("Click first 'Купить билеты' button"):
        cinema_list_page.click_first_buy_tickets_button()

    with allure.step("Wait for sessions page to load"):
        sessions_page = SessionsPage(driver)
        sessions_page.wait_for_page_to_load()

    with allure.step("Click first session time button"):
        sessions_page.click_first_session_button()

    with allure.step("Verify iframe appeared on the page"):
        assert sessions_page.is_iframe_visible(), "Iframe should appear after clicking session button"


@allure.story("Subscription")
@allure.title("Test subscription expansion flow")
@pytest.mark.ui
def test_expand_subscription(driver: WebDriver) -> None:
    with allure.step("Navigate to Kinopoisk main page"):
        main_page = MainPage(driver)
        main_page.open()

    with allure.step("Close modal window if present"):
        main_page.close_modal_if_present()

    with allure.step("Click 'Расширить подписку' button"):
        main_page.click_expand_subscription_button()

    with allure.step("Wait for subscription page to load"):
        time.sleep(5)

    with allure.step("Click 'Попробовать бесплатно' button"):
        main_page.click_try_free_button()

@allure.story("Online Cinema")
@allure.title("Test watch movie online flow")
@pytest.mark.ui
def test_watch_movie_online(driver: WebDriver) -> None:
    with allure.step("Navigate to Kinopoisk main page"):
        main_page = MainPage(driver)
        main_page.open()

    with allure.step("Close modal window if present"):
        main_page.close_modal_if_present()

    with allure.step("Click on HD Kinopoisk link"):
        main_page.click_online_cinema_link()

    with allure.step("Wait for online cinema page to load"):
        online_cinema_page = OnlineCinemaPage(driver)
        time.sleep(3)  # Даем время на полную загрузку страницы
        online_cinema_page.wait_for_page_to_load()

    with allure.step("Verify we are on HD Kinopoisk page"):
        assert online_cinema_page.is_on_online_cinema_page(), "Should be on HD Kinopoisk page"

    with allure.step("Select user profile"):
        time.sleep(2)  # Ждем стабилизации DOM
        online_cinema_page.click_user_avatar()

    with allure.step("Wait after profile selection"):
        time.sleep(2)  # Даем время на переход после выбора профиля

    with allure.step("Close modal window if present on HD page"):
        main_page.close_modal_if_present()

    with allure.step("Wait for film cards to load"):
        online_cinema_page.wait_for_film_cards()

    with allure.step("Click on first film card"):
        online_cinema_page.click_first_film_card()

    with allure.step("Wait for film slider to expand"):
        online_cinema_page.wait_for_film_slider()

    with allure.step("Click watch button"):
        online_cinema_page.click_watch_button()

    with allure.step("Wait for video player to load"):
        player_page = PlayerPage(driver)
        player_page.wait_for_player_to_load()
