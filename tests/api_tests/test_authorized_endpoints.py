import pytest
from .base_test import BaseTest


class TestAuthorizedEndpoints(BaseTest):
    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.authenticate(cls)

    def test_create_booking(self):
        payload = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        response = self.api_client.post('/booking', json=payload)
        assert response.status_code == 200
        self.booking_id = response.json()['bookingid']

    def test_update_booking(self):
        updated_payload = {
            "firstname": "James",
            "lastname": "Brown",
            "totalprice": 222,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2019-01-01",
                "checkout": "2020-01-01"
            },
            "additionalneeds": "Lunch"
        }
        response = self.api_client.put(f'/booking/{self.booking_id}', json=updated_payload)
        assert response.status_code == 200

    def test_delete_booking(self):
        response = self.api_client.delete(f'/booking/{self.booking_id}')
        assert response.status_code == 201  # У документації вказано 201 Created
