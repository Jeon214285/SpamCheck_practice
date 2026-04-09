from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)  # 테스트를 위해 앱을 연다.

def test_classify_api_contract():
    r = client.post("/classify", json={"text": "hello"})
    assert r.status_code == 200  # 200인지 아닌지
    data = r.json()
    assert "label" in data and "score" in data  # label이랑 score가 있는 딕셔너리가 있는지