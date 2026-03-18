# API-Test-Automation-Framework-for-RESTful-Services

This is an industry-level API automation framework built using Python, Pytest, and Requests.
## 🚀 Key Features

*   **Architecture**: Clean, scalable Service Object Model (SOM) / Page Object Model (POM) design.
*   **Client Layer**: Reusable `RestClient` wrapper for HTTP methods with built-in logging and retry logic.
*   **Service Layer**: Modular service classes for different API endpoints.
*   **Environment Support**: Configuration management for `dev`, `qa`, and `prod` environments.
*   **Data Driven**: Support for JSON test data and Pydantic models for schema validation.
*   **Reporting**: Automatic HTML reports (pytest-html) and Allure reporting support.
*   **Logging**: Structured logging using Python's `logging` module.
*   **Clean Code**: PEP 8 compliance, type hints, and descriptive docstrings.

## 📁 Project Structure

```text
api-automation-framework
│
├── api_client         # Reusable API request wrappers (Rest Client)
├── services           # Business logic / Service layer classes
├── config             # Centralized environment configuration
├── utils              # Shared utilities (logger, assertions, etc.)
├── test_data          # Test data (JSON) and Pydantic models
├── tests              # Pytest test cases
├── reports            # Test execution reports (HTML & Allure)
├── logs               # Execution log files
│
├── conftest.py        # Shared fixtures
├── requirements.txt   # Project dependencies
├── pytest.ini         # Pytest configuration
└── README.md          # Project documentation
```

## 🛠️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd api-automation-framework
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment (Optional):**
    Create a `.env` file in the root directory:
    ```env
    ENV=qa
    USERNAME=admin
    PASSWORD=password123
    ```

## 🧪 Running Tests

### Execute all tests:
```bash
pytest
```

### Run tests and generate HTML report:
The report is automatically generated in `reports/report.html` as configured in `pytest.ini`.

### Run tests with Allure:
1.  Run tests:
    ```bash
    pytest
    ```
2.  Serve Allure report (requires Allure CLI installed):
    ```bash
    allure serve reports/allure-results
    ```

## 📊 Logging
Logs are generated for every request and response.
*   **Console**: Real-time info logging.
*   **File**: Detailed debug logging in `logs/test_run_<timestamp>.log`.


*   Use type hints for better IDE support and code readability.
*   Add docstrings to all major classes and methods.
