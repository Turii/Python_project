import pytest
import requests
from pprint import pprint
from data.data import Data
from data.url import Urls


@pytest.fixture
def auth_url():
    return Urls.base_url + Urls.auth_url


def test_incorrect_password(auth_url):
    response = requests.post(auth_url, json={
        "login": "test_user",
        "password": "wrong_password"
    })

    assert response.status_code == 403, f"Unexpected status code: {response.status_code}"


def test_without_password(auth_url):
    response = requests.post(auth_url, json={
        "login": "test_user"
    })

    assert response.status_code == 422, f"Unexpected status code: {response.status_code}"


def test_short_login(auth_url):
    response = requests.post(auth_url, json={
        "login": "ab",
        "password": "qwerty12345"
    })

    assert response.status_code == 422, f"Unexpected status code: {response.status_code}"


def test_without_login(auth_url):
    response = requests.post(auth_url, json={
        "password": "qwerty12345"
    })

    assert response.status_code == 422, f"Unexpected status code: {response.status_code}"
