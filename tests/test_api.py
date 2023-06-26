from logging_monitor.main import app
from fastapi.testclient import TestClient
from fastapi import status

client = TestClient(app)


def test_get_app_meta_200():
    response = client.get("api/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "name": "logging-monitor",
        "version": "0.0.1",
        "description": "",
        "authors": ["DZIUREWICZ Piotr <dziurewiczpiotr@gmail.com>"],
    }


def test_put_app_meta_405():
    response = client.put("api/")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert response.json() == {"detail": "Method Not Allowed"}


def test_logs_put():
    response = client.post(
        "api/log", json={"level": "ERROR", "message": "This is error message"}
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"level": "ERROR", "message": "This is error message"}
