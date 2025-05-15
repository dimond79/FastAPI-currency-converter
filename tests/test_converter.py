from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_conversion():
    response = client.get("/convert?from_currency=USD&to_currency=EUR&amount=100")
    assert response.status_code == 200
    data = response.json()
    assert "converted_amount" in data
    assert data["from"] == "USD"
    assert data["to"] == "EUR"
    assert data["original_amount"] == 100