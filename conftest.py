import pytest
from playwright.sync_api import Page, Expect
from pages.cart_page import Cart
from utils.cookies_and_adv import register_cookie_handler

@pytest.fixture()
def login(page:Page):
    page.goto("/login")
    page.get_by_placeholder("Email Address").first.fill("adel.elakour@gmail.com")
    page.get_by_placeholder("Password").fill("123456789")
    page.get_by_role("button", name="Login").click()
    return page

@pytest.fixture()
def cart_with_products(page:Page):
    page.goto("/products")
    cart = Cart(page)
    cart.add_products_to_cart()
    return cart

@pytest.fixture()
def payment():
    def fill_payment_form(page: Page):
        page.locator("input[name='name_on_card']").fill("Adel Elakour")
        page.locator("input[name='card_number']").fill("2365478901")
        page.locator("input[name='cvc']").fill("333")
        page.locator("input[name='expiry_month']").fill("08")
        page.locator("input[name='expiry_year']").fill("2030")

    return fill_payment_form

@pytest.fixture(autouse=True)
def handle_cookies(page):
    register_cookie_handler(page)