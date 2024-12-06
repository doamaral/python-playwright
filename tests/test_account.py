"""Authentication Scenarios"""
import pytest
import logging
from utils.logger import logger

log = logger(logging.INFO)


@pytest.mark.parametrize('invoice_position, hotel_name, invoice_date, due_date, invoice_number, bookin_code, customer_details, room, checkin, checkout, totao_stay_count, total_stay_amount, deposit_now, tax_vat, total_amount',
                         [(1, 'Rendezvous Hotel', '14/01/2018', '15/01/2018', '110', '0875', 'JOHNY SMITH R2, AVENUE DU MAROC 123456', 'Superior Double', '14/01/2018', '15/01/2018', 1, '$150', 'USD $20.90', 'USD $19.00', 'USD $209.00')])
def test_should_match_given_values_for_invoice(login_before_each, invoice_position, hotel_name, invoice_date, due_date, invoice_number, bookin_code, customer_details, room, checkin, checkout, totao_stay_count, total_stay_amount, deposit_now, tax_vat, total_amount):
    """Test multiple possibilities of input for test authentication scenarios"""
    account_page = login_before_each
    account_page.open_detail_nth_invoice(invoice_position)
    # TODO: check values on invoice detail page
