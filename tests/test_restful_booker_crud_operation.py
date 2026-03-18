import pytest
from utils.assertions import assert_status_code, assert_response_contains, assert_schema
from test_data.models.booking_model import BookingResponse, BookingModel
from assertpy import assert_that

class TestRestfulBookerCRUD:
    """End-to-end tests for Restful Booker API."""

    @pytest.mark.order(1)
    def test_create_booking(self, service, create_booking_data, test_context):
        """Verify that a new booking can be created successfully."""
        response = service.create_booking(create_booking_data)
        
        assert_status_code(response, 200)
        assert_response_contains(response, "bookingid")
        
        # Schema validation using Pydantic
        assert_schema(response.json(), BookingResponse)
        
        # Save booking ID for next tests
        test_context["booking_id"] = response.json()["bookingid"]

    @pytest.mark.order(2)
    def test_get_booking(self, service, create_booking_data, test_context):
        """Verify that the created booking can be retrieved."""
        booking_id = test_context.get("booking_id")
        if not booking_id:
            pytest.skip("Booking ID not found in context")
            
        response = service.get_booking(booking_id)
        
        assert_status_code(response, 200)
        assert_schema(response.json(), BookingModel)
        
        # Data validation
        assert_that(response.json()["firstname"]).is_equal_to(create_booking_data["firstname"])

    @pytest.mark.order(3)
    def test_update_booking(self, service, update_booking_data, auth_token, test_context):
        """Verify that the booking can be updated with full payload."""
        booking_id = test_context.get("booking_id")
        if not booking_id:
            pytest.skip("Booking ID not found in context")
            
        response = service.update_booking(booking_id, update_booking_data, auth_token)
        
        assert_status_code(response, 200)
        assert_that(response.json()["additionalneeds"]).is_equal_to(update_booking_data["additionalneeds"])

    @pytest.mark.order(4)
    def test_delete_booking(self, service, auth_token, test_context):
        """Verify that the booking can be deleted."""
        booking_id = test_context.get("booking_id")
        if not booking_id:
            pytest.skip("Booking ID not found in context")
            
        response = service.delete_booking(booking_id, auth_token)
        
        # Restful Booker returns 201 Created for DELETE
        assert_status_code(response, 201)
        
        # Verify it's gone
        get_response = service.get_booking(booking_id)
        assert_status_code(get_response, 404)
