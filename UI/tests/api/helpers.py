from typing import Any, List


def validate_response_structure(
    data: dict[str, Any],
    required_fields: List[str]
) -> bool:
    return all(field in data for field in required_fields)


def validate_pagination(data: dict[str, Any]) -> bool:required_fields = ["docs", "total", "limit", "page", "pages"]
    return validate_response_structure(data, required_fields)


def validate_movie_structure(movie: dict[str, Any]) -> bool:
    return "id" in movie and (
        "name" in movie or "alternativeName" in movie
    )


def validate_person_structure(person: dict[str, Any]) -> bool:
    return "id" in person and (
        "name" in person or "enName" in person
    )
