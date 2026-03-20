"""
Pytest Configuration File
This file contains fixtures that are used across all tests
Fixtures are setup and teardown methods
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time

@pytest.fixture(scope="function")
def setup_chrome(request):
    """
    This fixture sets up the Chrome WebDriver, maximizes the window, and navigates to the GUVI website.
    It also ensures that the WebDriver is properly closed after the tests are completed.
    """

    # Setup
    print("\n" + "=" * 50)
    print("STARTING TEST - Initializing Chrome Browser")
    print("=" * 50)

    try:
        # Configure Chrome options
        chrome_options = Options()
        # Uncomment the line below to run browser in headless mode (no UI)
        # chrome_options.add_argument("--headless")

        # Initialize the Chrome WebDriver using webdriver_manager
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Initialize Chrome driver
        driver = webdriver.Chrome(options=chrome_options)

        driver.implicitly_wait(10)  # Implicit wait
        driver.maximize_window()  # Maximize browser window
        print("Chrome browser initialized successfully")

        # Store driver in request.cls to use in tests
        # request.cls.driver = driver

        yield driver  # This is where tests run

    except Exception as e:
        print(f"Error initializing Chrome: {str(e)}")
        raise

    finally:
        # Teardown
        print("\n" + "=" * 60)
        print("TEST COMPLETED - Closing Browser")
        print("=" * 60)
        try:
            # Clean up cookies and cache before closing
            driver.delete_all_cookies()
            time.sleep(0.5)
            driver.quit()
            print("✓ Browser closed successfully")
        except Exception as e:
            print(f"Error closing browser: {str(e)}")


@pytest.fixture(scope="function")
def setup_firefox(request):
    """
    Fixture to setup Firefox browser before tests and cleanup after
    """
    # Setup
    print("\n" + "=" * 60)
    print("STARTING TEST - Initializing Firefox Browser")
    print("=" * 60)

    try:
        # Initialize Firefox driver
        driver = webdriver.Firefox()

        driver.implicitly_wait(10)
        driver.maximize_window()

        print("Firefox browser initialized successfully")

        # request.cls.driver = driver

        yield driver

    except Exception as e:
        print(f"Error initializing Firefox: {str(e)}")
        raise

    finally:
        # Teardown
        print("\n" + "=" * 60)
        print("TEST COMPLETED - Closing Browser")
        print("=" * 60)
        try:
            # Clean up cookies and cache before closing
            driver.delete_all_cookies()
            time.sleep(0.5)
            driver.quit()
            print("✓ Browser closed successfully")
        except Exception as e:
            print(f"Error closing browser: {str(e)}")






