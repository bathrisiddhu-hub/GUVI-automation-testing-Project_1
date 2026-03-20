
# Automation Testing of GUVI EdTech Platform

## Website Link
The target application for this automation suite is: [https://www.guvi.in](https://www.guvi.in)

## Test Objective
The objective of this project is to automate the testing of the GUVI web application by simulating user actions and validating key UI functionalities. This includes verifying page behavior, accessibility of critical elements, navigation flows, and authentication processes.

## Tech Stack
- **Language**: Python 3.x
- **Browser Automation**: Selenium WebDriver
- **Test Framework**: Pytest
- **Reporting**: Pytest-HTML
- **Driver Management**: Webdriver-Manager

## Features
- **Cross-Browser Validation**: Configured to execute tests across both **Google Chrome** and **Mozilla Firefox**.
- **Page Object Model (POM)**: Implements separation between test logic and page-specific locators for maintainability.
- **Object-Oriented Design**: Utilizes inheritance and encapsulation to promote code reusability.
- **Resilient Execution**: Employs **Explicit Waits** and **Exception Handling** to manage dynamic elements.
- **Automated Reporting**: Generates detailed HTML reports using the `pytest-html` plugin.
- **Resource Management**: Uses Pytest fixtures to ensure all browser instances are properly closed after execution.

### Setup and Installation

1. **Clone the Repository**:
```bash
git clone https://github.com
cd GUVI-automation-testing-Project_1
```
2. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

### Running Tests
To execute the full test suite and generate an HTML report, run the following command in your terminal:
```bash
pytest
```
## Test Suite Coverage
```
The framework covers the following 10 critical test cases:
URL Validation: Verifies that the website loads successfully without errors.
Page Title: Confirms the title matches "GUVI | Learn to code in your native language".
Login Button Visibility: Checks if the Login button is displayed and clickable.
Sign-Up Button Visibility: Checks if the Sign-Up button is displayed and clickable.
Navigation Flow: Validates that clicking Sign-Up redirects correctly to the registration page.
Valid Login: Authenticates the user using valid credentials from the test data.
Invalid Login: Validates that appropriate error messages appear for incorrect credentials.
Menu Presence: Verifies "Courses", "LIVE Classes", and "Practice" are visible in the navigation.
Dobby Assistant: Confirms the Dobby Guvi Assistant widget is present on the homepage.
Logout Functionality: Validates successful session termination and redirection to the home/login page.
```
## Project Structure
```

text
├── pages/                # Page Object classes (Locators & Action Methods)
│   ├── base_page.py      # Base class with common Selenium wrappers
│   ├── home_page.py      # Homepage elements and actions
│   ├── login_page.py     # Login page elements and logout logic
│   └── register_page.py  # Registration page elements
├── test_data/            # External data for test scenarios
│   └── credentials.json  # Encapsulated user login credentials
├── tests/                # Automated test suites
│   └── test_guvi_webapp.py # Core test execution file for all scenarios
├── report/               # Local directory for generated HTML reports
├── conftest.py           # Global Pytest fixtures and cross-browser setup
├── pytest.ini            # Global framework configuration and CLI options
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```
