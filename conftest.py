import pytest
import os
import json
from services.restful_booker_service import RestfulBookerService
from config.config import Config
from utils.logger import logger

@pytest.fixture(scope="session")
def service():
    """Returns the RestfulBookerService instance."""
    return RestfulBookerService()

@pytest.fixture(scope="session")
def auth_token(service):
    """Generates an auth token for the session."""
    logger.info("Generating auth token for the test session")
    response = service.create_token(Config.USERNAME, Config.PASSWORD)
    token = response.json().get("token")
    if not token:
        pytest.fail("Failed to generate auth token")
    return token

@pytest.fixture(scope="session")
def create_booking_data():
    """Loads create booking data from JSON."""
    file_path = os.path.join(os.getcwd(), "test_data", "json", "create_booking.json")
    with open(file_path, "r") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def update_booking_data():
    """Loads update booking data from JSON."""
    file_path = os.path.join(os.getcwd(), "test_data", "json", "update_booking.json")
    with open(file_path, "r") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def test_context():
    """A dictionary to share data between tests."""
    return {}
