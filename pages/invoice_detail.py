""" Page object for Invoice Detail Page """
from playwright.sync_api import Page


class InvoiceDetailPage:
    """ Page object for Invoice Detail Page """

    def __init__(self, page: Page):
        self.page = page

        self.detail_header = self.page.locator('header h2')

        self.hotel_name = self.page.locator('h4')
        self.invoice_number = self.page.locator('h6')

        self.invoice_date = self.page.get_by_role('listitem').locator('nth=1')
        self.invoice_due_date = self.page.get_by_role(
            'listitem').locator('nth=2')

        self.invoice_details_table = self.page.locator('table tbody tr')
        self.booking_code = self.invoice_details_table.locator('nth=0')
        self.room = self.invoice_details_table.locator('nth=1')
        self.total_stay_count = self.invoice_details_table.locator('nth=2')
        self.total_stay_amount = self.invoice_details_table.locator('nth=3')
        self.checkin = self.invoice_details_table.locator('nth=4')
        self.checkout = self.invoice_details_table.locator('nth=5')

        self.customer_details = self.page.locator(
            'div:below(h5:text("Customer Details"))').first

        self.deposit_now = self.invoice_details_table.locator(
            'nth=6').locator('td').locator('nth=0')
        self.tax_vat = self.invoice_details_table.locator(
            'nth=6').locator('td').locator('nth=1')
        self.total_amount = self.invoice_details_table.locator(
            'nth=6').locator('td').locator('nth=2')

    def get_customer_details(self) -> str:
        """return customer details after clean it up"""
        raw_content = self.customer_details.inner_html()
        return raw_content.replace('<br>', ' ').replace('\n', ' ').strip()
