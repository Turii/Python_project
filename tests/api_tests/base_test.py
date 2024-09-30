import pytest
from src.api_client import APIClient
from config.config import load_config


class BaseTest:
    @classmethod
    def setup_class(cls):
        config = load_config()
        cls.api_client = APIClient(base_url=config['api']['base_url'])
        cls.auth_token = None

    def __init__(self):
        self.auth_token = None

    def authenticate(self):
        payload = {
            "username": "admin",
            "password": "password123"
        }
        response = self.api_client.post('/auth', json=payload)
        assert response.status_code == 200
        self.auth_token = response.json()['token']
        self.api_client.set_token(self.auth_token)


"""class BaseTest:
    @pytest.fixture(autouse=True, scope='class')
    def setup_class(cls):
        config = load_config()
        cls.api_client = APIClient(base_url=config['api']['base_url'])
        cls.auth_token = None

    def authenticate(self):
        #Метод для отримання токена авторизації
        config = load_config()
        payload = {
            "username": config['api']['username'],
            "password": config['api']['password']
        }
        response = self.api_client.post('/auth', json=payload)
        assert response.status_code == 200
        self.auth_token = response.json()['token']
        self.api_client.set_token(self.auth_token)
"""
