from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_health_status():
    response = client.get("/health-status")
    assert response.status_code == 200
    assert response.json() == {"status": "Service is up and running!"}
