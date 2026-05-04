
import requests

BASE_URL = "https://postman-echo.com"

def test_1_get_with_params():
    params = {"city": "Moscow", "page": "1"}
    response = requests.get(f"{BASE_URL}/get", params=params)
    assert response.status_code == 200
    assert response.json()["args"] == params

def test_2_post_with_json():
    payload = {"product": "Laptop", "price": 1500}
    response = requests.post(f"{BASE_URL}/post", json=payload)
    assert response.status_code == 200
    assert response.json()["json"] == payload

def test_3_post_with_form():
    form_data = {"username": "tester", "action": "login"}
    response = requests.post(f"{BASE_URL}/post", data=form_data)
    assert response.status_code == 200
    assert response.json()["form"] == form_data

def test_4_put_request():
    payload = {"id": 1, "status": "updated"}
    response = requests.put(f"{BASE_URL}/put", json=payload)
    assert response.status_code == 200
    assert response.json()["json"] == payload

def test_5_delete_request():
    response = requests.delete(f"{BASE_URL}/delete")
    assert response.status_code == 200