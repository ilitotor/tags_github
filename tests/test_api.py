from starlette.testclient import TestClient
from main import app

client = TestClient(app)

def test_return_must_be_a_json():
    response = client.get("/repository/")
    assert response.headers["Content-Type"] == "application/json"
