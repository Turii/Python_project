import pytest
from .base_test import BaseTest


class TestPublicEndpoints(BaseTest):
    def test_get_booking_ids(self):
        response = self.api_client.get('/booking')
        assert response.status_code == 200

    def test_get_booking(self):
        booking_id = 1
        response = self.api_client.get(f'/booking/{booking_id}')
        assert response.status_code == 200

    """def test_get_booking_ids(self):
        response = self.api_client.get('/booking')
        assert response.status_code == 200

    def test_get_booking(self):
        booking_id = 1  # Можна динамічно отримувати існуючий ID
        response = self.api_client.get(f'/booking/{booking_id}')
        assert response.status_code == 200 """
