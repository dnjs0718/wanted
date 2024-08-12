import os
from collections.abc import Generator

import pytest
from anyio.abc import BlockingPortal
from starlette_testclient import TestClient
from tortoise.contrib.test import finalizer, initializer

from common.config.db_conn import TORTOISE_ORM
from main import create_app


@pytest.fixture(scope="module")
def client() -> Generator:
    os.environ["API_ENV"] = "test"

    db_url = os.environ['TEST_DB_URL']

    if os.environ['API_ENV'] != "test":
        msg = "API_ENV must be 'test'"
        raise Exception(msg)

    if not db_url:
        msg = "required TEST_DB_URL"
        raise Exception(msg)

    if db_url.split("@")[1].split("/")[0] != "localhost":
        msg = "db host must be 'localhost' in test environment"
        raise Exception(msg)

    if db_url.split("/")[-1].split("?")[0].split("_")[0] != "test":
        msg = "schema name must start with 'test'"
        raise Exception(msg)

    initializer(
        modules=TORTOISE_ORM["apps"]["models"]["models"],
        db_url=db_url,
    )

    with TestClient(create_app()) as c:
        yield c
        
    finalizer()
    

@pytest.fixture(scope="module")
def portal(client: TestClient) -> BlockingPortal:
    assert client.portal
    return client.portal