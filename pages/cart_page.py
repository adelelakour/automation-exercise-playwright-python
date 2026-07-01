from _pytest._py import path
from playwright.sync_api import Page
from utils.cookies_and_adv import close_ad_if_visible

from pages.base_page import BasePage
from utils import cookies_and_adv


class Cart(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.products_tab = page.get_by_role("link", name="Products")
        self.first_product = page.get_by_role("link", name="View Product").first
        self.first_product_quantity = page.locator('#quantity')

        self.second_product = page.get_by_role("link", name="View Product").nth(1)
        self.second_product_quantity = page.locator('#quantity')

        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")

        self.continue_shoping = page.get_by_role("button", name="Continue Shopping")
        self.view_cart_button = page.get_by_role("link", name="View Cart")

        #delete button
        self.remove_item = page.locator(".cart_quantity_delete")

        #adv_close_button
        self.adv_close_button = page.frame_locator('iframe[name="aswift_3"]').get_by_role("button", name="Close ad")

    def add_products_to_cart(self):

            self.first_product.click()
            close_ad_if_visible(self.page)

            self.first_product_quantity.fill("3")
            self.add_to_cart_button.click()
            self.continue_shoping.click()

            self.products_tab.click()

            # Second product
            self.second_product.click()

            # self.adv_button.click()
            self.second_product_quantity.fill("2")
            self.add_to_cart_button.click()

            self.view_cart_button.click()

    def remove_products_from_cart(self):
        self.remove_item.first.click()