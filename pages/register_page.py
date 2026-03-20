"""
Register Page Object
Contains all elements and methods related to the Register Page
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):

    """
    register page class that inherits from base page
    contains locators and methods specific to the register page
    """
    # define locators for register page elements
    signup_page = (By.XPATH, "//h2[contains(text(), 'Sign Up')]") # locator for signup page title

    def is_signup_page_displayed(self):
        """
        check if the signup page is displayed by verifying the presence of the signup page title
        """
        result = self.is_element_displayed(self.signup_page)
        print(f"Signup page displayed: {result}")
        return result




