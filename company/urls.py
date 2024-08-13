from fastapi import FastAPI, Depends


from company.routes import search, detail
from common.config.consts import LANGUAGE_HEADER


def include_routers(app: FastAPI):
    app.include_router(
        search.router,
        tags=["회사"],
        prefix="/search",
        dependencies=[Depends(LANGUAGE_HEADER)],
    )
    app.include_router(
        detail.router,
        tags=["회사"],
        prefix="/companies",
        dependencies=[Depends(LANGUAGE_HEADER)],
    )
