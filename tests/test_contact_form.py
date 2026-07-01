from playwright.sync_api import  Playwright, Page, expect
from pathlib import Path
from pages.contact_us_page import ContactUs
from utils.cookies_and_adv import accept_cookies

class Test_ContactUs():

    def test_contactUs_valid(self, page:Page):

        PROJECT_ROOT = Path(__file__).resolve().parents[1]
        SHIRT_IMAGE = PROJECT_ROOT / "images" / "shirt.jpg"

        page.goto("/contact_us")
        # page.on("dialog", lambda dialog: dialog.accept())
        contact_us = ContactUs(page)
        contact_us.test_contactUs_form("adel", "adel.elakour@gmail.com", "Refund Request",
                                       "Hi, I bought this shirt, but the quality is lower than I expected. Could you please issue me a refund?", SHIRT_IMAGE)
        expect(page.get_by_text("Get In Touch")).to_be_visible()


    def test_contactUs_invalid(self, page:Page):
        page.goto("/contact_us")
        contact_us = ContactUs(page)
        contact_us.test_contactUs_form("adel", "adel.elakour@gmail.com", "Refund Request",
                                       "Hi, I bought this shirt, but the quality is lower than I expected. Could you please issue me a refund?", "images/shirt.jpg")
        expect(page.)

