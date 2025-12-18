import pytest
import allure
from utils.api_client import PoiskKinoAPIClient


@allure.story("Movies API")
@allure.title("Получение списка фильмов")
@pytest.mark.api
def test_get_movies_list(api_client: PoiskKinoAPIClient) -> None:
    with allure.step("Отправка запроса на получение списка фильмов"):
        response = api_client.get_movies(page=1, limit=10)

    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == 200, \
            f"Ожидался статус код 200, получен {response.status_code}"

    with allure.step("Проверка структуры ответа"):
        data = response.json()
        assert "docs" in data, "В ответе отсутствует поле 'docs'"
        assert isinstance(data["docs"], list), \
            "Поле 'docs' должно быть списком"

    with allure.step("Проверка наличия данных в ответе"):
        assert len(data["docs"]) > 0, \
            "Список фильмов не должен быть пустым"

    with allure.step("Проверка структуры данных фильма"):
        movie = data["docs"][0]
        assert "id" in movie, "В данных фильма отсутствует поле 'id'"
        assert "name" in movie or "alternativeName" in movie, \
            "В данных фильма отсутствуют названия"


@allure.story("Movies API")
@allure.title("Получение фильма по ID")
@pytest.mark.api
def test_get_movie_by_id(api_client: PoiskKinoAPIClient) -> None:
    test_movie_id = 263531  # Deadpool

    with allure.step(
        f"Отправка запроса на получение фильма с ID {test_movie_id}"
    ):
        response = api_client.get_movie_by_id(test_movie_id)

    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == 200, \
            f"Ожидался статус код 200, получен {response.status_code}"

    with allure.step("Проверка структуры ответа"):
        data = response.json()
        assert "id" in data, "В ответе отсутствует поле 'id'"

    with allure.step("Проверка соответствия ID"):
        assert data["id"] == test_movie_id, \
            f"Ожидался ID {test_movie_id}, получен {data['id']}"


@allure.story("Movies API")
@allure.title("Поиск фильмов по запросу")
@pytest.mark.api
def test_search_movies(api_client: PoiskKinoAPIClient) -> None:
    search_query = "deadpool"

    with allure.step(
        f"Отправка запроса на поиск фильмов с запросом '{search_query}'"
    ):
        response = api_client.search_movies(
            query=search_query,
            page=1,
            limit=10
        )

    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == 200, \
            f"Ожидался статус код 200, получен {response.status_code}"

    with allure.step("Проверка структуры ответа"):
        data = response.json()
        assert "docs" in data, "В ответе отсутствует поле 'docs'"
        assert isinstance(data["docs"], list), \
            "Поле 'docs' должно быть списком"

    with allure.step("Проверка наличия результатов поиска"):
        assert len(data["docs"]) > 0, \
            f"Поиск по запросу '{search_query}' не вернул результатов"


@allure.story("Movies API")
@allure.title("Получение случайного фильма")
@pytest.mark.api
def test_get_random_movie(api_client: PoiskKinoAPIClient) -> None:
    with allure.step("Отправка запроса на получение случайного фильма"):
        response = api_client.get_random_movie()

    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == 200, \
            f"Ожидался статус код 200, получен {response.status_code}"

    with allure.step("Проверка структуры ответа"):
        data = response.json()
        assert "id" in data, "В ответе отсутствует поле 'id'"

    with allure.step("Проверка наличия данных о фильме"):
        assert "name" in data or "alternativeName" in data, \
            "В данных фильма отсутствуют названия"


@allure.story("Persons API")
@allure.title("Получение списка персон")
@pytest.mark.api
def test_get_persons_list(api_client: PoiskKinoAPIClient) -> None:
    with allure.step("Отправка запроса на получение списка персон"):
        response = api_client.get_persons(page=1, limit=10)

    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == 200, \
            f"Ожидался статус код 200, получен {response.status_code}"

    with allure.step("Проверка структуры ответа"):
        data = response.json()
        assert "docs" in data, "В ответе отсутствует поле 'docs'"
        assert isinstance(data["docs"], list), \
            "Поле 'docs' должно быть списком"

    with allure.step("Проверка наличия данных в ответе"):
        assert len(data["docs"]) > 0, \
            "Список персон не должен быть пустым"

    with allure.step("Проверка структуры данных персоны"):
        person = data["docs"][0]
        assert "id" in person, "В данных персоны отсутствует поле 'id'"
        assert "name" in person or "enName" in person, \
            "В данных персоны отсутствуют имена"


@allure.story("Movies API")
@allure.title("Проверка пагинации списка фильмов")
@pytest.mark.api
def test_movies_pagination(api_client: PoiskKinoAPIClient) -> None:
    limit = 5

    with allure.step(
        f"Отправка запроса на получение первой страницы "
        f"с лимитом {limit}"
    ):
        response_page1 = api_client.get_movies(page=1, limit=limit)

    with allure.step("Проверка статус кода первой страницы"):
        assert response_page1.status_code == 200, \
            f"Ожидался статус код 200, получен {response_page1.status_code}"

    with allure.step(
        f"Проверка количества элементов на странице (не более {limit})"
    ):
        data_page1 = response_page1.json()
        assert len(data_page1["docs"]) <= limit, \
            f"Количество элементов превышает лимит {limit}"

    with allure.step("Отправка запроса на получение второй страницы"):
        response_page2 = api_client.get_movies(page=2, limit=limit)

    with allure.step("Проверка статус кода второй страницы"):
        assert response_page2.status_code == 200, \
            f"Ожидался статус код 200, получен {response_page2.status_code}"

    with allure.step("Проверка различия данных между страницами"):
        data_page2 = response_page2.json()
        ids_page1 = {movie["id"] for movie in data_page1["docs"]}
        ids_page2 = {movie["id"] for movie in data_page2["docs"]}
        assert ids_page1 != ids_page2, \
            "Данные на разных страницах должны отличаться"


@allure.story("Movies API")
@allure.title("Проверка несуществующего ID фильма")
@pytest.mark.api
def test_get_movie_by_invalid_id(api_client: PoiskKinoAPIClient) -> None:
    invalid_movie_id = 999999999

    with allure.step(
        f"Отправка запроса на получение фильма "
        f"с несуществующим ID {invalid_movie_id}"
    ):
        response = api_client.get_movie_by_id(invalid_movie_id)

    with allure.step(
        "Проверка статус кода ответа (должен быть 404 или пустой ответ)"
    ):
        assert response.status_code in [404, 400], \
            f"Ожидался статус код 404 или 400, получен {response.status_code}"

