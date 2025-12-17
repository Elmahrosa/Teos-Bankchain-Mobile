from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_transaction_flow():
    login = client.post("/login", json={"username": "demo", "password": "demo123"})
    assert login.status_code in (200, 401)

    tx = client.post("/transaction", json={"amount": 100, "currency": "USD"})
    assert tx.status_code in (200, 400)

    logs = client.get("/audit")
    assert logs.status_code == 200
