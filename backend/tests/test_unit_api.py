from fastapi.testclient import TestClient
from backend.main import app  # adjust if your entrypoint is different

client = TestClient(app)

def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_login_route():
    payload = {"username": "demo", "password": "demo123"}
    response = client.post("/login", json=payload)
    assert response.status_code in (200, 401)

