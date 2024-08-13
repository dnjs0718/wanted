from fastapi.security import APIKeyHeader


LANGUAGE_HEADER = APIKeyHeader(name="x-wanted-language", auto_error=False)

LANGUAGE_REQUIRED_LIST = [
    "/search",
    "/companies",
]

LANGUAGE_REQUIRED_REGEX_LIST = [
    "/companies/.*",
]

EXCEPT_LIST = [
    "/docs",
    "/openapi.json",
]
