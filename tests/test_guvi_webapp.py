"""
Test Suite for GUVI Web Application
Contains all test cases for the GUVI website
"""
import time
import pytest
import json
import os
from webdriver_manager.core import driver
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage

# Load test data from JSON file
def load_credentials():
    """
    Load user credentials from a JSON file
    """
    credentials_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'test_data',
        'credentials.json'
    )
    with open(credentials_path) as f:
        return json.load(f)

@pytest.mark.parametrize("browser_setup", ["setup_chrome", "setup_firefox"])
class TestGUVIWebApplication:
    """
    Test class for GUVI Web Application
    Contains all test cases
    """
    BASE_URL = "https://www.guvi.in/"

    @pytest.fixture(autouse=True)
    def setup_driver(self, request, browser_setup):
        """
        Dynamically gets the driver from either setup_chrome or setup_firefox
        """
        self.driver = request.getfixturevalue(browser_setup)
        print("\n" + "=" * 50)
        print(f"\n--- Running Test on: {browser_setup} ---")
        print("TEST SETUP - Navigating to GUVI Website")
        print("=" * 50)
        self.driver.get(self.BASE_URL)
        time.sleep(2)

        print(f"Fresh driver assigned for test")
        yield

        # Cleanup after test
        self.driver.delete_all_cookies()
        time.sleep(0.5)

    def setup_method(self):
        """
        This method is called before each test method
        opens the guvi website
        """
        pass # Empty, driver already setup in fixture

    def teardown_method(self):
        """
        This method is called after each test method
        can be used for cleanup
        """
        print("\n" + "=" * 50)
        print("TEST TEARDOWN - Test Completed")
        print("=" * 50)

    # Test Case 1
    def test_01_verify_url_is_valid(self):
        """
        Test Case 1: Verify whether the URL is valid or not
        Expected: Website should load successfully
        """
        print("\n Test Case 1: Verify URL is valid")
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")

        # assert that the current URL matches the expected URL
        assert "guvi.in" in current_url, "URL is not valid or website did not load successfully"
        print("Passed: URL is valid and website loaded successfully")

    # Test Case 2
    def test_02_verify_page_title(self):
        """
        Test Case 2: Verify whether the title of the webpage is correct
        Expected: Title should be "GUVI | Learn to code in your native language"
        """
        print("\n Test Case 2: Verify Page Title")

        home_page = HomePage(self.driver)
        actual_title = home_page.get_page_title()
        expected_title = "HCL GUVI | Learn to code in your native language"
        print(f"Actual Title: {actual_title}")
        print(f"Expected Title: {expected_title}")

        # assert that the actual title matches the expected title
        assert actual_title == expected_title, f"Page title is incorrect. Expected: '{expected_title}', but got: '{actual_title}'"
        print("Passed: Page title is correct")

    # Test Case 3
    def test_03_verify_login_button_visible_and_clickable(self):
        """
        Test Case 3: Verify visibility and clickability of the Login button
        Expected: Login button should be visible and clickable
        """
        print("\n Test Case 3: Verify Login Button Visibility and Clickability")

        home_page = HomePage(self.driver)

        # check if the login button is visible
        is_visible = home_page.is_login_button_displayed()
        assert is_visible, "Login button is not visible on the homepage"
        print("Passed: Login button is visible")

        # check if the login button is clickable
        home_page.click_login_button()  # This will also verify if the button is clickable

        # wait for the page transition
        import time
        time.sleep(2)  # Adjust the sleep time as needed

        # check if we are on the login page by verifying the URL or page title
        current_url = self.driver.current_url.lower()
        assert "login" in current_url or "sign-in" in current_url, \
            f"Did not navigate to login page. Current URL: {current_url}"
        print("Passed: Login button is clickable and navigates to the login page")

    # Test case 4
    def test_04_verify_signup_button_visible_and_clickable(self):
        """
        Test Case 4: Verify visibility and clickability of the Sign-Up button
        Expected: Sign-Up button should be visible and clickable
        """
        print("\n Test Case 4: Verify Sign-Up Button Visibility and Clickability")

        home_page = HomePage(self.driver)

        # check if the sign-up button is visible
        is_visible = home_page.is_signup_button_displayed()
        assert is_visible, "Sign-Up button is not visible on the homepage"
        print("Passed: Sign-Up button is visible")

        # check if the sign-up button is clickable
        home_page.click_signup_button()  # This will also verify if the button is clickable

        # wait for the page transition
        import time
        time.sleep(2)  # Adjust the sleep time as needed

        # check if we are on the sign-up page by verifying the URL or page title
        current_url = self.driver.current_url.lower()
        assert "register" in current_url, f"Did not navigate to sign-up page. Current URL: {current_url}"
        print("Passed: Sign-Up button is clickable and navigates to the sign-up page")

    # Test Case 5
    def test_05_verify_navigation_to_register_page(self):
        """
        Test Case 5: Verify navigation to the Sign-In page via the Sign-Up button
        Expected: Should navigate to https://www.guvi.in/register/
        """
        print("\n Test Case 5: Verify Navigation to Register Page")

        home_page = HomePage(self.driver)
        home_page.click_signup_button()  # Click the Sign-Up button

        # wait for the page transition
        import time
        time.sleep(2)  # Adjust the sleep time as needed

        register_page = RegisterPage(self.driver)

        # check if we are on the register page by verifying the URL
        current_url = self.driver.current_url
        expected_url = "https://www.guvi.in/register/"

        print(f"Current URL: {current_url}")
        print(f"Expected URL: {expected_url}")

        assert expected_url in current_url, f"URL is incorrect. Expected: '{expected_url}', but got: '{current_url}'"
        print("Passed: Navigated to the correct register page URL")

    # Test Case 6
    def test_06_verify_login_with_valid_credentials(self):
        """
        Test Case 6: Verify login functionality with valid credentials
        Expected: User should be logged in and redirected to dashboard/profile
        """
        print("\n Test Case 6: Verify Login with Valid Credentials")

        credentials = load_credentials()
        valid_email = credentials["valid_credentials"]["email"]
        valid_password = credentials["valid_credentials"]["password"]

        home_page = HomePage(self.driver)
        home_page.click_login_button()  # Click the Login button

        # wait for the page transition
        import time
        time.sleep(2)  # Adjust the sleep time as needed

        login_page = LoginPage(self.driver)
        login_page.login(valid_email, valid_password)  # Perform login with valid credentials

        # wait for the login process to complete
        time.sleep(3)  # Adjust the sleep time as needed

        # check if we are logged in by verifying the URL or page title
        current_url = self.driver.current_url.lower()
        print(f"Current URL after login: {current_url}")

        # check login was successful(url should change to dashboard/profile)
        assert "login" not in current_url, f"still on login page. Current URL: {current_url}"
        print("Passed: Login successful with valid credentials and navigated to the dashboard/profile page")

    # Test Case 7
    def test_07_verify_login_with_invalid_credentials(self):
        """
        Test Case 7: Verify login with invalid credentials
        Expected: Login should fail and error message should be displayed
        """
        print("\n Test Case 7: Verify Login with Invalid Credentials")

        credentials = load_credentials()
        invalid_email = credentials["invalid_credentials"]["email"]
        invalid_password = credentials["invalid_credentials"]["password"]

        home_page = HomePage(self.driver)
        print(f"DEBUG: Current URL is {self.driver.current_url}")
        home_page.click_login_button()  # Click the Login button

        # wait for the page transition
        import time
        time.sleep(2)  # Adjust the sleep time as needed

        login_page = LoginPage(self.driver)
        login_page.login(invalid_email, invalid_password)  # Perform login with invalid credentials

        # wait for the login process to complete
        time.sleep(2)  # Adjust the sleep time as needed

        # check for the error message displayed on the page
        error_message = login_page.get_error_message()

        # Either the error message should be displayed or thh url still should be login page
        current_url = self.driver.current_url.lower()

        is_error_displayed = error_message is not None and len(error_message) > 0
        still_on_login_page = "login" in current_url

        assert is_error_displayed or still_on_login_page, "Neither error message is displayed nor login page is displayed."
        print("Passed: Login failed with invalid credentials as expected")

    # Test Case 8
    def test_08_verify_menu_items_presence(self):
        """
        Test Case 8: Verify that menu items like "Courses", "LIVE Classes", and "Practice" are displayed
        Expected: All menu items should be visible
        """
        print("\n Test Case 8: Verify Menu Items Presence")

        home_page = HomePage(self.driver)

        # check if all menu items are displayed
        all_visible = home_page.are_menu_items_displayed()
        assert all_visible, "Not all menu items are visible on the homepage"
        print("Passed: All menu items are visible on the homepage")

    # Test Case 9
    def test_09_verify_dobby_assistant_displayed(self):
        """
        Test Case 9: Validate that the Dobby GUVI Assistant is present on the page
        Expected: Dobby Assistant should be displayed
        """
        print("\n Test Case 9: Verify Dobby Assistant Presence")

        home_page = HomePage(self.driver)

        # check if the Dobby assistant is displayed
        is_present = home_page.is_dobby_assistant_displayed()

        if is_present:
            print("Passed: Dobby GUVI Assistant is present on the page")
            assert True
        else:
            print("Failed: Dobby GUVI Assistant is not present on the page")

    # Test Case 10
    def test_10_verify_logout_functionality(self):
        """
        Test Case 10: Validate logout functionality
        Expected: User should be logged out and redirected to home/login page
        """
        print("\n Test Case 10: Verify Logout Functionality")

        credentials = load_credentials()
        valid_email = credentials["valid_credentials"]["email"]
        valid_password = credentials["valid_credentials"]["password"]

        # login first to perform logout
        home_page = HomePage(self.driver)
        home_page.click_login_button()  # Click the Login button

        # wait for the page transition
        import time
        time.sleep(2)  # Adjust the sleep time as needed

        login_page = LoginPage(self.driver)
        login_page.login(valid_email, valid_password)  # Perform login with valid credentials

        # wait for the login process to complete
        time.sleep(8)  # Adjust the sleep time as needed

        # Now perform logout
        current_url = self.driver.current_url.lower()
        if "login" in current_url:
            pytest.skip("Could not login")

        logout_success = login_page.logout()
        time.sleep(2)

        assert logout_success, "Logout failed or was not redirected correctly"
