import logging
import pytest
from playwright.sync_api import Page
from utils.logger import logger


log = logger(logging.DEBUG)


@pytest.fixture(scope='function', autouse=True)
def before_each(request, page: Page):
    """Actions take place before each test"""
    log.info('running test: %s', request.node.name)
    return page
