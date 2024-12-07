""" Pytest hooks and configurations"""
import os
import logging
import pytest
import allure
from playwright.sync_api import Page
from dotenv import load_dotenv
from pages.login import LoginPage
from pages.account import AccountPage
from utils.logger import logger

load_dotenv(override=True)
log = logger(logging.INFO)


@allure.title("Test setup: open browser and open base page.")
@pytest.fixture
def before_each(request, page: Page):
    """Actions take place before each test"""
    log.info('openning browser on page: %s', os.getenv("BASE_URL"))
    page.goto(os.getenv("BASE_URL"))
    log.info('running test: %s', request.node.name)
    return page, os.getenv("BASE_URL")


@allure.title("Test setup: Open browser and log in")
@pytest.fixture
def login_before_each(request, page: Page) -> AccountPage:
    """Authentication actions that should take place before tests"""
    log.info('running test: %s', request.node.name)
    page.goto(os.getenv("BASE_URL"))
    login_page = LoginPage(page)
    login_page.do_login(os.getenv("USERNAME"), os.getenv("PASSWORD"))
    return AccountPage(page)
