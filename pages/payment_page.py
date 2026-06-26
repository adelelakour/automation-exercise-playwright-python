from pages.base_page import BasePage

class Payment(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.checkout_button = page.locator("a.check_out")
        self.notes = page.locator("textarea.form-control")
        self.place_order_button = page.locator('a[href="/payment"]')
        self.name_on_card = page.locator("input[name=\"name_on_card\"]")
        self.card_number = page.locator("input[name=\"card_number\"]")
        self.cvc = page.get_by_role("textbox", name="ex.")
        self.exp_month = page.get_by_role("textbox", name="MM")
        self.exp_year = page.get_by_role("textbox", name="YYYY")
        self.pay_button = page.get_by_role("button", name="Pay and Confirm Order")

    def do_checkout(self, note, name_on_card, card_number, cvc, expiration_month, expiration_year):
        self.checkout_button.click()
        self.notes.fill(note)
        self.place_order_button.click()
        self.name_on_card.fill(name_on_card)
        self.card_number.fill(card_number)
        self.cvc.fill(cvc)
        self.exp_month.fill(expiration_month)
        self.exp_year.fill(expiration_year)
        self.pay_button.click()

