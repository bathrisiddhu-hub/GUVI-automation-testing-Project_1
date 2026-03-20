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
- **Cross-Browser Validation**: Configured to execute tests across both Google Chrome and Mozilla Firefox.
- **Page Object Model (POM)**: Implements separation between test logic and page-specific locators for maintainability.
- **Object-Oriented Design**: Utilizes inheritance and encapsulation to promote code reusability.
- **Resilient Execution**: Employs Explicit Waits and Exception Handling to manage dynamic elements.
- **Automated Reporting**: Generates detailed HTML reports using the `pytest-html` plugin.
- **Resource Management**: Uses Pytest fixtures to ensure all browser instances are properly closed after execution.

## Setup and Installation
To set up and run this project locally, follow these steps:

Clone the Repository:

git clone https://github.com/imranc07/Mini_Project_1.git
cd Mini_Project_1
Create a Virtual Environment (optional but recommended):

python3 -m venv env
source env/bin/activate  # For Windows, use `env\Scripts\activate`
Install Dependencies:

pip install -r requirements.txt
Set Up Environment Variables:

Create a .env file in the root directory to store sensitive information such as login credentials and URLs. Example:
BASE_URL=https://example.com
USER_EMAIL=test@example.com
USER_PASSWORD=yourpassword
Running Tests
To execute tests, use the following commands:

Run All Tests:

pytest
Generate HTML Report:

pytest --html=Reports/test_report.html
Run Tests by Marker (e.g., only "login" tests):

pytest TestScripts/test_HomePage.py::test_guvi_url
Headless Browser Execution:

You can set up tests to run in Headless mode directly in your test script.
Project Structure:

## Project Structure

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

git clone https://github.com
cd GUVI-automation-testing-Project_1
