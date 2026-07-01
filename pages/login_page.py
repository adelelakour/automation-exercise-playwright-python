from pytest_playwright.pytest_playwright import playwright

from pages.base_page import BasePage
from playwright.sync_api import TimeoutError as PlayrightTimeOut

class Login(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.login_tab = page.get_by_role("link", name=" Signup / Login")
        self.login_email_address = page.get_by_placeholder("Email Address").first
        self.login_password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def login_process(self, email, password):
        self.login_tab.click()
        self.login_email_address.fill(email)
        self.login_password.fill(password)
        self.login_button.click()

class Signup(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.page = page
        self.signup_name = page.get_by_placeholder("Name")
        self.signup_email = page.get_by_placeholder("Email Address").nth(1)
        self.signup_button = page.get_by_role("button", name="Signup")

        self.user_password = page.get_by_role("textbox", name="Password *", exact=True)
        self.birthdate_day = page.locator("#days")
        self.birthdate_month = page.locator("#months")
        self.birthdate_year = page.locator("#years")

        self.newsletter = page.get_by_role("checkbox", name="Sign up for our newsletter!")
        self.offers = page.get_by_role("checkbox", name="Receive special offers from")

        self.first_name = page.get_by_role("textbox", name="First name *")
        self.last_name = page.get_by_role("textbox", name="Last name *")
        self.address = page.get_by_role("textbox", name="Address *")

        self.country = page.get_by_label("Country", exact=False)
        self.state =   page.get_by_role("textbox", name="State *")
        self.city =   page.get_by_role("textbox", name="City *")
        self.zip =   page.locator("#zipcode")
        self.mobile =   page.get_by_role("textbox", name="Mobile Number *")
        self.create_account_button = page.get_by_role("button", name="Create Account")


    # def accept_popup_if_visible(self):
    #     try:
    #         with self.page.expect_event("dialog", timeout=5000) as dialog_info:
    #             dialog.acc

    def create_account_valid_data(self, signup_name, signup_email, gender, password, day, month,
                       year, first_name, last_name, address, country, state, city, zip, mobile_number):

        #first_signup_page
        self.signup_name.fill(signup_name)
        self.signup_email.fill(signup_email)
        self.signup_button.click()

        #second_signup_page
        self.page.get_by_role("radio", name=gender).check()
        self.user_password.fill(password)
        self.birthdate_day.select_option(day)
        self.birthdate_month.select_option(month)
        self.birthdate_year.select_option(year)
        self.newsletter.check()
        self.offers.check()

        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.address.fill(address)
        self.country.select_option(country)
        self.state.fill(state)
        self.city.fill(city)
        self.zip.fill(zip)
        self.mobile.fill(mobile_number)

        self.create_account_button.click()


    def create_account_existing_email(self, signup_name, signup_email):
        #first_signup_page
        self.signup_name.fill(signup_name)
        self.signup_email.fill(signup_email)
        self.signup_button.click()

    def create_account_invalid_email(self, signup_name, signup_email):
        #first_signup_page
        self.signup_name.fill(signup_name)
        self.signup_email.fill(signup_email)
        self.signup_button.click()

    def create_account_invalid_email(self, signup_name, signup_email):
        #first_signup_page
        self.signup_name.fill(signup_name)
        self.signup_email.fill(signup_email)
        self.signup_button.click()


