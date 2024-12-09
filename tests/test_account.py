"""Authentication Scenarios"""
import logging
import pytest
import allure
from playwright.sync_api import expect
from utils.logger import logger

log = logger(logging.INFO)


@allure.title("Check invoice detail values")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC003")
@pytest.mark.parametrize('invoice_position, hotel_name, invoice_date, due_date, invoice_number, booking_code, customer_details, room, checkin, checkout, total_stay_count, total_stay_amount, deposit_now, tax_vat, total_amount',
                         [(1, 'Rendezvous Hotel', '14/01/2018', '15/01/2018', '110', '0875', 'JOHNY SMITH R2, AVENUE DU MAROC 123456', 'Superior Double', '14/01/2018', '15/01/2018', '1', '$150', 'USD $20.90', 'USD $19.00', 'USD $209.00')])
def test_should_match_given_values_for_invoice(login_before_each, invoice_position, hotel_name, invoice_date, due_date, invoice_number, booking_code, customer_details, room, checkin, checkout, total_stay_count, total_stay_amount, deposit_now, tax_vat, total_amount):
    """Test multiple possibilities of input for test authentication scenarios"""
    account_page = login_before_each

    # invoice detail page is now on a different context, a new tab
    # be aware that if we want to get back to previous context
    # we should use the account_page object
    invoice_detail_page = account_page.open_detail_nth_invoice(
        invoice_position)

    # hotel name
    expect(invoice_detail_page.hotel_name).to_contain_text(hotel_name)

    # invoice number
    expect(invoice_detail_page.invoice_number).to_contain_text(invoice_number)

    # invoice dates
    expect(invoice_detail_page.invoice_date).to_contain_text(invoice_date)
    expect(invoice_detail_page.invoice_due_date).to_contain_text(due_date)

    # booking/stay details
    expect(invoice_detail_page.booking_code).to_contain_text(booking_code)
    expect(invoice_detail_page.room).to_contain_text(room)
    expect(invoice_detail_page.total_stay_count).to_contain_text(total_stay_count)
    expect(invoice_detail_page.total_stay_amount).to_contain_text(
        total_stay_amount)
    expect(invoice_detail_page.checkin).to_contain_text(checkin)
    expect(invoice_detail_page.checkout).to_contain_text(checkout)

    # customer details
    assert invoice_detail_page.get_customer_details() == customer_details

    # billings details
    expect(invoice_detail_page.deposit_now).to_contain_text(deposit_now)
    # expect(invoice_detail_page.tax_vat).to_contain_text(tax_vat)
    # expect(invoice_detail_page.total_amount).to_contain_text(total_amount)
