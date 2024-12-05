"""Authentication Scenarios"""
import logging
from playwright.sync_api import expect
from utils.logger import logger
from pages.login import LoginPage

log = logger(logging.INFO)


def test_should_get_authenticated_success(before_each):
    """Test multiple possibilities of input for test authentication scenarios"""
    page, base_url = before_each
    login_page = LoginPage(page)
    login_page.do_login('demouser', 'abc123')
    expect(page).to_have_url(f"{base_url}/account")
