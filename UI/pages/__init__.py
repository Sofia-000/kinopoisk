"""Pages package."""
from .base_page import BasePage
from .main_page import MainPage
from .media_page import MediaPage
from .article_page import ArticlePage
from .film_page import FilmPage
from .cinema_list_page import CinemaListPage
from .sessions_page import SessionsPage
from .online_cinema_page import OnlineCinemaPage
from .player_page import PlayerPage

__all__ = ["BasePage", "MainPage", "MediaPage", "ArticlePage", "FilmPage", "CinemaListPage", "SessionsPage", "OnlineCinemaPage", "PlayerPage"]
