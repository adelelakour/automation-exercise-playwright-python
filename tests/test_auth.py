from playwright.sync_api import  Playwright, Page, expect
from pages.login_page import Login, Signup, ContactUs
import random


class Test_Login():

    def test_login_valid_credentials(self, page:Page):
        page.goto("/")
        login = Login(page)
        login.login_process("adel.elakour@gmail.com", "123456789")
        expect(page.get_by_text("Delete Account")).to_be_visible()

    def test_login_invalid_credentials(self, page:Page):
        page.goto("/")
        login = Login(page)
        login.login_process("adel.elakour@gmail.com", "22558899")
        expect(page.get_by_text("Your email or password is incorrect")).to_be_visible()

    def test_login_blank_entries(self, page:Page):
        page.goto("https://automationexercise.com/")
        login = Login(page)
        login.login_process("", "")
        eval_msg = login.login_email_address.evaluate("element => element.validationMessage")
        assert eval_msg == "Please fill out this field."

class Test_Signup():

    def test_create_account_valid_data(self, page:Page):
        page.goto("/login")
        signUp = Signup(page)
        rand_num = random.randint(0,3000)
        signUp.create_account("Dodo", f"Madeha{rand_num}@gmail.com", "Mr. ", "123456789", "23", "August", "1992",
                              "madeha", "dola", "Dumyat Gadeda", "Canada",
                              "Ontario", "Toronto", "20784", "01086379016")

        expect(page.get_by_text("Account Created", exact=False)).to_be_visible()


    def test_create_account_invalid_data(self, page:Page):
        page.goto("/login")
        signUp = Signup(page)
        signUp.create_account_invalid_email("Dodo", "adelgmail.com")

        eval_msg = signUp.signup_email.evaluate("element => element.validationMessage")
        assert "Please include an" in eval_msg

class Test_ContactUs():

    def test_contactUs_valid(self, page:Page):
        page.goto("/contact_us")
        page.on("dialog", lambda dialog: dialog.accept())
        contact_us = ContactUs(page)
        contact_us.test_contactUs_form("adel", "adel.elakour@gmail.com", "Refund Request",
                                       "Hi, I bought this shirt, but the quality is lower than I expected. Could you please issue me a refund?", "images/shirt.jpg")
        expect(page.get_by_text("Get In Touch")).to_be_visible()


    def test_contactUs_invalid(self, page:Page):
        page.goto("/contact_us")
        contact_us = ContactUs(page)
        contact_us.test_contactUs_form("adel", "adel.elakour@gmail.com", "Refund Request",
                                       "Hi, I bought this shirt, but the quality is lower than I expected. Could you please issue me a refund?", "images/shirt.jpg")


