from api_client.rest_client import RestClient
from config.config import Config
from typing import Dict

class BaseService:
    """Base category for all service classes."""
    
    def __init__(self):
        self.client = RestClient()
        self.config = Config
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get_auth_headers(self, token: str) -> Dict[str, str]:
        """Returns headers with Cookie-based auth for Restful Booker."""
        headers = self.headers.copy()
        headers["Cookie"] = f"token={token}"
        return headers
    
    def get_basic_auth_headers(self) -> Dict[str, str]:
        """Returns headers with Basic Auth if needed (though Restful Booker usually uses token)."""
        # Alternatively, for Restful Booker, many endpoints use Cookie: token=...
        # But some might allow Basic Auth.
        import base64
        auth_str = f"{self.config.USERNAME}:{self.config.PASSWORD}"
        encoded_auth = base64.b64encode(auth_str.encode()).decode()
        headers = self.headers.copy()
        headers["Authorization"] = f"Basic {encoded_auth}"
        return headers
