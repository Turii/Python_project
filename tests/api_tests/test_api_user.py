import json
import pytest
import requests
from pprint import pprint
from data.data import Data
from data.url import Urls


class Test:
    post_data = Data()
    base_url = Urls()
    status_OK = 200

    @pytest.mark.regression
    def test_create_user(self):
        response = requests.post(f"{self.base_url.base_url}{self.base_url.post_url}", json=self.post_data.data)

        assert response.status_code == 201, f"Unexpected status code: {response.status_code}"

    # payload = json.dumps({
    #   "first_name": "Frieda",
    #   "last_name": "Ortiz",
    #   "company_id": 1
    # })
    # headers = {
    #   'Content-Type': 'application/json'
    # }
    #
    # response = requests.request("POST", url, headers=headers, data=payload)
    #
    # print(response.text)

    def test_get_user(self):
        url = "https://send-request.me/api/users/24418"
        response = requests.get(url)
        user_data = response.json()
        pprint(response.json())
        pprint(response.status_code)

        assert response.status_code == self.status_OK, f"Unexpected status code: {response.status_code}"

        expected_first_name = "Frieda"
        expected_last_name = "Ortiz"
        assert user_data['first_name'] == expected_first_name, f"Unexpected user name: {user_data['first_name']}"
        assert user_data['last_name'] == expected_last_name, f"Unexpected last user name: {user_data['last_name']}"


base_url = 'https://restful-booker.herokuapp.com/booking'
auth_url = 'https://restful-booker.herokuapp.com/auth'


# def sum_it(x, y):
#     return x + y
#
# def test_equal():
#     assert sum_it(5, 7) == 8
def test_get_token():
    auth_data = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(auth_url, json=auth_data)
    token = response.json()["token"]
    print(token)
    assert response.status_code == 200
    return  token