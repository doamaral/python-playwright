"""Page Object that handles Logged pages header"""
from playwright.sync_api import Page


class HeaderPage:
    """Page Object that handles Logged pages header"""

    def __init__(self, page: Page):
        self.page = page
        self.header_title = self.page.locator('span.navbar-brand')
        self.logout_button = self.page.get_by_text('Logout')

    def logout_user(self):
        """End session"""
        self.logout_button.click()
