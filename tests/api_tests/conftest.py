import pytest
from src.api_client import APIClient
from config.config import load_config

@pytest.fixture(scope='session')
def api_client():
    config = load_config()
    return APIClient(base_url=config['api']['base_url'])