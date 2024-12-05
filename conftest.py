""" Pytest hooks and configurations"""
import os
import logging
import pytest
from playwright.sync_api import Page
from utils.logger import logger


log = logger(logging.INFO)


@pytest.fixture(scope='function', autouse=True)
def before_each(request, page: Page):
    """Actions take place before each test"""
    log.info('openning browser on page: %s', os.getenv("BASE_URL"))
    page.goto(os.getenv("BASE_URL"))
    log.info('running test: %s', request.node.name)
    return page, os.getenv("BASE_URL")
