import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL: str = os.getenv("BASE_URL", "https://www.kinopoisk.ru")
    BROWSER: str = os.getenv("BROWSER", "chrome")
    HEADLESS: bool = os.getenv("HEADLESS", "False").lower() == "true"
    IMPLICIT_WAIT: int = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT: int = int(os.getenv("EXPLICIT_WAIT", "15"))
    API_BASE_URL: str = os.getenv('API_BASE_URL', 'https://api.poiskkino.dev')
    API_KEY: Optional[str] = os.getenv('API_KEY')
    TIMEOUT: int = int(os.getenv('TIMEOUT', '30'))

    @classmethod
    def get_headers(cls) -> dict[str, str]:
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        if cls.API_KEY:
            headers['X-API-KEY'] = f'Bearer {cls.API_KEY}'
        return headers

config = Config()
