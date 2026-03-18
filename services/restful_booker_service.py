from services.base_service import BaseService
from requests import Response
from typing import Dict, Any

class RestfulBookerService(BaseService):
    """Service layer for Restful Booker API."""
    
    BOOKING_ENDPOINT = "/booking"
    AUTH_ENDPOINT = "/auth"

    def create_token(self, username: str, password: str) -> Response:
        """Create a new auth token."""
        payload = {
            "username": username,
            "password": password
        }
        return self.client.post(self.AUTH_ENDPOINT, json_data=payload)

    def get_booking_ids(self) -> Response:
        """Get all booking IDs."""
        return self.client.get(self.BOOKING_ENDPOINT)

    def get_booking(self, booking_id: int) -> Response:
        """Get a specific booking by ID."""
        return self.client.get(f"{self.BOOKING_ENDPOINT}/{booking_id}")

    def create_booking(self, booking_data: Dict[str, Any]) -> Response:
        """Create a new booking."""
        return self.client.post(self.BOOKING_ENDPOINT, json_data=booking_data)

    def update_booking(self, booking_id: int, booking_data: Dict[str, Any], token: str) -> Response:
        """Update an existing booking (Full update)."""
        headers = self.get_auth_headers(token)
        return self.client.put(f"{self.BOOKING_ENDPOINT}/{booking_id}", json_data=booking_data, headers=headers)

    def partial_update_booking(self, booking_id: int, partial_data: Dict[str, Any], token: str) -> Response:
        """Partial update of an existing booking."""
        headers = self.get_auth_headers(token)
        return self.client.patch(f"{self.BOOKING_ENDPOINT}/{booking_id}", json_data=partial_data, headers=headers)

    def delete_booking(self, booking_id: int, token: str) -> Response:
        """Delete a booking."""
        headers = self.get_auth_headers(token)
        return self.client.delete(f"{self.BOOKING_ENDPOINT}/{booking_id}", headers=headers)
