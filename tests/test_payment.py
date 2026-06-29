from playwright.sync_api import  Playwright, Page, expect
from pages.payment_page import Payment

class Test_Payment():

    def test_valid_payment(self, login, cart_with_products, page:Page):

        order = Payment(page)
        order.do_checkout("Please drop the order at doorstep",
                          "Adel Elakour",
                          "2658745",
                          "333",
                          "08",
                          "2030"
                          )
        expect(page.get_by_text("Order Placed")).to_be_visible()

