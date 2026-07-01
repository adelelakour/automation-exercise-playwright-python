from playwright.sync_api import  Playwright, Page, expect
from pages.cart_page import Cart
from utils.cookies_and_adv import accept_cookies


class TestCart():

    def test_add_products_to_cart(self, page:Page ):
        page.goto("/")
        cart = Cart(page)
        cart.add_products_to_cart()
        expect(page.get_by_role("button", name="3")).to_be_visible()
        expect(page.get_by_role("button", name="2")).to_be_visible()

    def test_remove_items_from_cart(self, cart_with_products, page):
        remove_item = Cart (page)
        remove_item.remove_products_from_cart()
        expect(page.locator(".cart_quantity_delete").first).to_be_visible()
