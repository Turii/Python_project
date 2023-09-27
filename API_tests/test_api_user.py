import json
import requests
from pprint import pprint


def test_create_user():
    url = "https://send-request.me/api/users"

    data = {
        "first_name": "Frieda",
        "last_name": "Ortiz",
        "company_id": 1
    }
    response = requests.post(url, json=data)

    assert response.status_code == 201, f"Unexpected status code: {response.status_code}"
    pprint(response.json())
    print()
    pprint(response.json())
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


def test_get_user():
    url = "https://send-request.me/api/users/24418"
    response = requests.get(url)
    pprint(response.json())
    pprint(response.status_code)