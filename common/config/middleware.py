from collections.abc import Callable
from re import match

from fastapi import Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from common.config.consts import (
    LANGUAGE_REQUIRED_LIST,
    LANGUAGE_REQUIRED_REGEX_LIST,
    EXCEPT_LIST,
)
from company.db.schema import Language


class LanguageValidatorMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self: BaseHTTPMiddleware, request: Request, call_next: Callable
    ) -> Callable:
        headers = request.headers
        url = request.url.path
        request.state.language = None
        if url not in EXCEPT_LIST:
            if (
                url in LANGUAGE_REQUIRED_LIST or await url_check(url)
            ) and "x-wanted-language" not in headers:
                return JSONResponse(
                    status_code=401, content={"detail": "language required"}
                )

            if not (
                language := await Language.get_or_none(
                    short_name=headers.get("x-wanted-language")
                )
            ):
                return JSONResponse(
                    status_code=404, content={"detail": "language not found"}
                )

            request.state.language = language

        response = await call_next(request)
        return response


async def url_check(path: str) -> bool:
    pattern = f'(?:{"|".join(LANGUAGE_REQUIRED_REGEX_LIST)})'
    return bool(match(pattern, path))
