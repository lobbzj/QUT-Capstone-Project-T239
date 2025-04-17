import requests

def test_homepage():
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200
    assert "Testing" in response.text

def test_greet():
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200
    assert response.json()["message"] == "Testing"

