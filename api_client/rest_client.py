import json
import requests
from typing import Any, Dict, Optional
from utils.logger import logger
from config.config import Config
import time

class RestClient:
    """
    A reusable request wrapper for GET, POST, PUT, DELETE with logging and retry mechanism.
    """
    
    def __init__(self, base_url: str = Config.BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def request(
        self, 
        method: str, 
        endpoint: str, 
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Any] = None,
        json_data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout: int = Config.TIMEOUT,
        retries: int = Config.RETRY_COUNT
    ) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        
        # Merge default headers if needed, or just use provided
        request_headers = headers or {"Content-Type": "application/json", "Accept": "application/json"}
        
        attempt = 0
        while attempt < retries:
            try:
                logger.info(f"Sending {method} request to {url}")
                if json_data:
                    logger.debug(f"Request Body: {json.dumps(json_data, indent=2)}")
                
                response = self.session.request(
                    method=method,
                    url=url,
                    params=params,
                    data=data,
                    json=json_data,
                    headers=request_headers,
                    timeout=timeout
                )
                
                self._log_response(response)
                
                # Check for flaky errors that might need retry (e.g., 5xx)
                if 500 <= response.status_code <= 599:
                    logger.warning(f"Server error {response.status_code} received. Retrying... (Attempt {attempt + 1}/{retries})")
                    attempt += 1
                    time.sleep(Config.RETRY_DELAY)
                    continue
                
                return response
                
            except requests.exceptions.RequestException as e:
                logger.error(f"Request failed: {str(e)}")
                attempt += 1
                if attempt == retries:
                    raise
                time.sleep(Config.RETRY_DELAY)

    def _log_response(self, response: requests.Response):
        logger.info(f"Response Status Code: {response.status_code}")
        try:
            if response.text:
                logger.debug(f"Response Body: {json.dumps(response.json(), indent=2)}")
        except ValueError:
            logger.debug(f"Response Body (text): {response.text}")

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("DELETE", endpoint, **kwargs)

    def patch(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("PATCH", endpoint, **kwargs)
