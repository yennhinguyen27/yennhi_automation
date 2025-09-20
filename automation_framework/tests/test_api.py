import pytest
import requests
from automation_framework.helper.API_helper import APIHelper

api = APIHelper(base_url="https://reqres.in/api")

def test_get_single_user():
    response = api.get_request("/users/2")
    print("GET status:", response.status_code)
    print("GET body:", response.json())

    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2
    assert response.json()["data"]["email"] == "janet.weaver@reqres.in"


# def test_post_create_user():
#     url = "https://reqres.in/api/users"
#     payload = {
#         "name": "morpheus",
#         "job": "leader"
#     }
#     headers = {"Content-Type": "application/json"}

#     response = requests.post(url, json=payload, headers=headers)

#     print("Status:", response.status_code)
#     print("Body:", response.json())

#     assert response.status_code == 201