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
        assert  user_data['first_name'] == expected_first_name, f"Unexpected user name: {user_data['first_name']}"
        assert user_data['last_name'] == expected_last_name, f"Unexpected last user name: {user_data['last_name']}"