from requests import Response
from assertpy import assert_that, soft_assertions
from utils.logger import logger

def assert_status_code(response: Response, expected_code: int):
    """Utility to assert status code with logging."""
    logger.info(f"Asserting status code: Expected {expected_code}, Got {response.status_code}")
    assert_that(response.status_code).is_equal_to(expected_code)

def assert_response_contains(response: Response, key: str):
    """Utility to assert key presence in JSON response."""
    data = response.json()
    logger.info(f"Asserting key '{key}' in response")
    assert_that(data).contains(key)

def assert_schema(data: dict, model_class):
    """Utility to validate data against a Pydantic model."""
    try:
        logger.info(f"Validating schema against {model_class.__name__}")
        model_class(**data)
    except Exception as e:
        logger.error(f"Schema validation failed: {str(e)}")
        raise AssertionError(f"Schema validation failed for {model_class.__name__}: {str(e)}")
