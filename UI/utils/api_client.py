"""API клиент для работы с Kinopoisk API."""

from typing import Optional, Any
import requests
from requests import Response
from config.config import config


class PoiskKinoAPIClient:
    """Клиент для работы с Kinopoisk API."""

    def __init__(self, base_url: Optional[str] = None, api_key: Optional[str] = None):
        self.base_url = base_url or config.API_BASE_URL
        self.api_key = api_key or config.API_KEY
        self.session = requests.Session()
        self.timeout = config.TIMEOUT
        
        # Устанавливаем заголовки
        self._setup_headers()

    def _setup_headers(self) -> None:
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        # Добавляем X-API-KEY если ключ указан
        if self.api_key:
            headers['X-API-KEY'] = self.api_key
        
        self.session.headers.update(headers)

    def get_movies(
        self,
        page: int = 1,
        limit: int = 10,
        params: Optional[dict[str, Any]] = None
    ) -> Response:
        url = f"{self.base_url}/v1.4/movie"
        query_params = params or {}
        query_params.update({'page': page, 'limit': limit})
        return self.session.get(url, params=query_params, timeout=self.timeout)

    def get_movie_by_id(self, movie_id: int) -> Response:
        url = f"{self.base_url}/v1.4/movie/{movie_id}"
        return self.session.get(url, timeout=self.timeout)

    def search_movies(
        self,
        query: str,
        page: int = 1,
        limit: int = 10
    ) -> Response:
        url = f"{self.base_url}/v1.4/movie/search"
        params = {
            'page': page,
            'limit': limit,
            'query': query
        }
        return self.session.get(url, params=params, timeout=self.timeout)

    def get_random_movie(self) -> Response:
        url = f"{self.base_url}/v1.4/movie/random"
        return self.session.get(url, timeout=self.timeout)

    def get_persons(
        self,
        page: int = 1,
        limit: int = 10,
        params: Optional[dict[str, Any]] = None
    ) -> Response:
        url = f"{self.base_url}/v1.4/person"
        query_params = params or {}
        query_params.update({'page': page, 'limit': limit})
        return self.session.get(url, params=query_params, timeout=self.timeout)

    def close(self) -> None:
        """Закрыть сессию."""
        self.session.close()