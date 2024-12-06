""" Page object for Account page """
from playwright.sync_api import Page
from pages.components.header import HeaderPage
from pages.invoice_detail import InvoiceDetailPage


class AccountPage:
    """Page Object that handles Account page"""

    def __init__(self, page: Page):
        self.page = page
        self.header = HeaderPage(self.page)
        self.table_rows = self.page.locator('div.row').locator('a')

    def open_detail_nth_invoice(self, position: int) -> InvoiceDetailPage:
        """ Return Invoice Detail clicking on the nth Invoice link """
        count = self.table_rows.count()
        index = position - 1

        if index < 0 or index >= count:
            raise ValueError(f"position must be between 1 and {
                             count}, got {position}.")
        self.table_rows.nth(index).click()
        return InvoiceDetailPage(self.page)
