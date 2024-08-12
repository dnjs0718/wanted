import asyncio

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from os import environ

API_ENV = environ.get("API_ENV", "local")
DB_URL = environ.get("DB_URL")

TORTOISE_ORM = {
    "connections": {
        "default": DB_URL if API_ENV != "test" else environ.get("TEST_DB_URL"),
    },
    "apps": {
        "models": {
            "models": [
                "aerich.models",
                "company.db.schema",
            ],
            "default_connection": "default",
        },
    },
}


class RDBconnect:
    def __init__(self, app: FastAPI = None, **kwargs):
        if app is not None:
            self.init_app(app=app, **kwargs)
            self.LOCK = asyncio.Lock()

    def init_app(self, app: FastAPI = None, **kwargs):
        is_test = kwargs.setdefault('TEST_MODE', False)

        if is_test:
            register_tortoise(
                app,
                config=TORTOISE_ORM,
                generate_schemas=True,
                add_exception_handlers=True
            )

        register_tortoise(
            app,
            config=TORTOISE_ORM,
            add_exception_handlers=True
        )

rdb = RDBconnect()
