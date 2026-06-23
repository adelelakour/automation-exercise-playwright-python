from playwright.sync_api import Page, expect

class BasePage:

    def __init__(self, page:Page):
        self.page = page

    def home_page(self):
        return self.page.get_by_role("link", name=" Home").click()

    def products_page(self):
        return self.page.get_by_role("link", name=" Products").click()

    def cart_page(self):
        return self.page.get_by_role("link", name=" Cart").click()

    def login_page(self):
        return self.page.get_by_role("link", name=" Signup / Login").click()

    def contact_us(self):
        return self.page.get_by_role("link", name=" Contact us").click()
