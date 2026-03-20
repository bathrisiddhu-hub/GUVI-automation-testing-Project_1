"""
Home Page Object
Contains all elements and methods related to the Home Page
"""

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    """
    home page class that inherits from base page
    contains locators and methods specific to the home page
    """

    # define locators for home page elements
    login_button = (By.ID, "login-btn")
    #login_button = (By.XPATH, "(//button[@id='login-btn'])[1]") # locator for login button
    signup_button = (By.XPATH, "(//button[contains(text(), 'Sign up')])[1]") # locator for signup button
    course_menu = (By.XPATH, "(//p[text()='Courses'])[1]") # locator for course menu
    live_classes_menu = (By.XPATH, "(//p[text()='LIVE Classes'])[1]") # locator for live classes menu
    practice_menu = (By.XPATH, "(//p[text()='Practice'])[1]") # locator for practice menu
    DOBBY_ASSISTANT = (By.XPATH, "//span[@id='zs_fl_chat']") # locator for Dobby assistant menu

    def click_login_button(self):
        """
        click on the login button
        """
        self.click(self.login_button)

    def click_signup_button(self):
        """
        click on the signup button
        """
        self.click(self.signup_button)

    def is_login_button_displayed(self):
        """
        check if the login button is displayed
        """
        result = self.is_element_displayed(self.login_button)
        print(f"Login button displayed: {result}")
        return result

    def is_signup_button_displayed(self):
        """
        check if the signup button is displayed
        """
        result = self.is_element_displayed(self.signup_button)
        print(f"Signup button displayed: {result}")
        return result

    def are_menu_items_displayed(self):
        """
        check if the course menu, live classes menu, and practice menu are displayed
        """
        course_menu_displayed = self.is_element_displayed(self.course_menu)
        live_classes_menu_displayed = self.is_element_displayed(self.live_classes_menu)
        practice_menu_displayed = self.is_element_displayed(self.practice_menu)
        print(f"Course menu displayed: {course_menu_displayed}")
        all_menus_displayed = course_menu_displayed and live_classes_menu_displayed and practice_menu_displayed
        print(f"All menu items displayed: {all_menus_displayed}")
        return all_menus_displayed

    def is_dobby_assistant_displayed(self):
        """
        check if the Dobby assistant menu is displayed
        """
        result = self.is_element_displayed(self.DOBBY_ASSISTANT)
        print(f"Dobby Assistant displayed: {result}")
        return result






