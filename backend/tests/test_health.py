# backend/tests/test_health.py
from fastapi.testclient import TestClient
from backend.main import app  # adjust import if your FastAPI app entrypoint differs

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
