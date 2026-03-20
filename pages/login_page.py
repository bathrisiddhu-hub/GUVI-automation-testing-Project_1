"""
Login Page Object
Contains all elements and methods related to the Login Page
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time

class LoginPage(BasePage):

    """
    login page class that inherits from base page
    contains locators and methods specific to the login page
    """

    # define locators for login page elements
    email_input = (By.ID, "email")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-btn")
    error_message = (By.XPATH, "//div[text()='Incorrect Email or Password']") # locator for error
    profile_dropdown = (By.XPATH, "//img[@alt='Profile']") # locator for profile dropdown
    logout_button = (By.XPATH, "(//p[contains(text(), 'Sign Out')])[1]")  # locator for logout button

    def enter_email(self, email):
        """
        enter email into the email input field
        """
        self.send_keys(self.email_input, email)

    def enter_password(self, password):
        """
        enter password into the password input field
        """
        self.send_keys(self.password_input, password)

    def click_login_button(self):
        """ Click on the login button """
        self.click(self.login_button)
        time.sleep(2)  # Wait for the login process to complete


    def login(self, email, password):
        """ Perform the login action by entering email, password and clicking the login button """
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self):
        """
        Get the error message displayed on the page
        """
        try:
            error_text = self.get_text(self.error_message)
            print(f"Error message found: {error_text}")
            return error_text
        except:
            print("Error message not found.")
            return None

    def logout(self):
        try:
            # Step 1: Click profile avatar (The logs show this part works)
            print("Clicking profile avatar...")
            self.click(self.profile_dropdown)

            # Step 2: WAIT for the menu to actually appear
            # Sometimes a simple sleep isn't enough; let's ensure the menu is there
            time.sleep(3)

            # Step 3: Click Sign Out button
            # Try using a direct text match if your current SIGN_OUT locator is failing
            print("Clicking Sign Out button...")

            # You can try updating your SIGN_OUT variable to:
            # (By.XPATH, "//button[contains(text(),'Sign Out')]")
            self.click(self.logout_button)

            time.sleep(4)  # Wait for redirection to complete

            # Step 4: Verification
            current_url = self.driver.current_url.lower()
            print(f"Final URL after logout: {current_url}")

            # Returns True if we moved away from the dashboard back to home/login
            return "login" in current_url or "guvi.in" in current_url

        except Exception as e:
            print(f"Logout failed due to error: {str(e)}")
            return False

        except Exception as e:
            print(f"Logout failed due to error: {e}")
            return False


