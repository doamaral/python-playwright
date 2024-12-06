""" Page object for Invoice Detail Page """
from playwright.sync_api import Page


class InvoiceDetailPage:
    """ Page object for Invoice Detail Page """

    def __init__(self, page: Page):
        self.page = page
