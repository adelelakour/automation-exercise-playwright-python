from _pytest._py import path
from pytest_playwright.pytest_playwright import page

from pages.base_page import BasePage

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


    def add_products_to_cart(self):
        self.first_product.click()
        self.first_product_quantity.first.fill("3")
        self.add_to_cart_button.click()
        self.continue_shoping.click()

        self.products_tab.click()
        self.second_product.click()
        self.first_product_quantity.first.fill("2")
        self.add_to_cart_button.click()
        self.view_cart_button.click()

    def remove_products_from_cart(self):
        self.remove_item.first.click()