from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_health_status() -> None:
    response = client.get("/health-status")
    assert response.status_code == 200
    assert response.json() == {"status": "Service is up and running!"}
