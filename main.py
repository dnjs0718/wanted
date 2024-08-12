from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
from uvicorn import run

from common.config.db_conn import rdb
from common.config.middleware import LanguageValidatorMiddleware
from company.urls import include_routers as company_routers


def create_app():
    app = FastAPI(
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            ),
            Middleware(LanguageValidatorMiddleware)
        ]
    )
    
    rdb.init_app(app)
    
    company_routers(app)
    
    return app

app = create_app()


if __name__ == "__main__":
    run(app="main:app", host="0.0.0.0", port=8001, reload=True)