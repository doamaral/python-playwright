""" Page object for Login page """
import re
import allure
from playwright.sync_api import Page


class LoginPage:
    """Page Object that handles Login page"""

    def __init__(self, page: Page):
        self.page = page
        self.username_field = self.page.locator('[name="username"]')
        self.password_field = self.page.locator('[name="password"]')
        self.submit_button = self.page.get_by_role(
            'button', name=re.compile("login", re.IGNORECASE))
        self.error_message = self.page.get_by_role('alert')

    @allure.step("Login with username {username} and password {password}")
    def do_login(self, username, password):
        """Method that handles all login process"""
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.submit_button.click()
