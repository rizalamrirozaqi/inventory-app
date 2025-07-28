import requests

def test_health_endpoint():
    res = requests.get("http://localhost:5000/health")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"