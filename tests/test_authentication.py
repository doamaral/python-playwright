"""Authentication Scenarios"""
import logging
import pytest
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


@pytest.mark.parametrize('username, password', [('Demouser', 'abc123'), ('demouser_', 'xyz'), ('demouser', 'nananana'), ('demouser', 'abc123'),])
def test_should_not_get_authenticaded(before_each, username, password):
    """test multiple inputs for wrong credentials"""
    page, base_url = before_each

    login_page = LoginPage(page)
    login_page.do_login(username, password)

    expect(page).to_have_url(f"{base_url}/")
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text(
        'Wrong username or password.')
