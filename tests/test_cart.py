from playwright.sync_api import  Playwright, Page, expect
import re

def test_add_multiple_products_to_cart(page:Page):

    page.goto("https://automationexercise.com/")
    first_product = page.locator(".col-sm-4").nth(1)
    first_product.locator(".productinfo a").click()
    page.get_by_role("button", name="Continue Shopping").click()

    second_product = page.locator(".col-sm-4").nth(4)
    second_product.locator(".productinfo a").click(force=True)
    page.locator(".modal-content a[href='/view_cart']").click()

    expect(page.locator("#cart_info_table tbody tr")).to_have_count(2)

