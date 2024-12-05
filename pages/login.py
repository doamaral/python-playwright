
import os
from dotenv import load_dotenv

load_dotenv()


class LoginPage:
    """Page Object that handles Login page"""

    def __init__(self, page):
        self.page = page
        self.username_field = self.page.get_by_role("input", name="username")
        self.password_field = self.page.get_by_role("input", name="password")

    def do_login(self, username, password):
        """Method that handles all login process"""
        self.page.goto(os.getenv("BASE_URL"))
        self.username_field.fill(username)
        self.password_field.fill(password)
