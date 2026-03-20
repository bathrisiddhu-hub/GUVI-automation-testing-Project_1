"""
Base Page Class
This class contains common methods that are used across all pages.
All page classes will inherit from this class.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class BasePage:
    """
    base class for all pages
    contains common methods like click, send_keys, wait, etc.
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) # wait for 10 seconds
        self.timeout = 10

    def open(self, url):
        """
        Open the specified URL in the browser.
        args:
            url (str): The URL to open.
        """
        self.driver.get(url)
        print(f"Opened URL: {url}")

    def click(self, locator):
        """
        click on the element specified by the locator.
        args:
            locator (tuple): A tuple containing the locator strategy and locator value.
        """
        element = self.wait_for_element_clickable(locator)
        element.click()
        print(f"Clicked on element: {locator}")

    def send_keys(self, locator, text):
        """
        wait for the element to be visible and send keys to it.
        """
        element = self.wait_for_element(locator)
        element.send_keys(text)
        print(f"Sent keys to element: {locator}")

    def wait_for_element(self, locator):
        """
        Wait for the element to be visible and return it
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        """
        Wait for the element to be clickable and return it
        """
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))

    def get_text(self, locator):
        """
        get the text of the element specified by the locator.
        """
        element = self.wait_for_element(locator)
        return element.text

    def is_element_displayed(self, locator):
        """
        Check if the element specified by the locator is present on the page.
        """
        try:
            element = self.driver.find_element(*locator)
            is_displayed = element.is_displayed()
            print(f"Element {locator} is displayed: {is_displayed}")
            return is_displayed
        except Exception as e:
            print(f"Element {locator} not found or not displayed: {str(e)}")
            return False

    def get_page_title(self):
        """
        Get the title of the current page.
        """
        return self.driver.title

    def get_current_url(self):
        """
        Get the current URL of the page.
        """
        return self.driver.current_url

    def take_screenshot(self, file_name):
        """
        Take a screenshot of the current page
        """
        self.driver.save_screenshot(f"reports/{file_name}.png")
        print(f"Screenshot saved as: {file_name}.png")

    def switch_new_window(self):
        """
        Switch to the new window that is opened
        """
        self.driver.switch_to.window(self.driver.window_handles[-1])
        print("Switched to new window")















