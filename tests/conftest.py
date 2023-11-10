import pytest
from fastapi.testclient import TestClient

from app.main import server


@pytest.fixture()
def client():
    with TestClient(server) as client:
        yield client
