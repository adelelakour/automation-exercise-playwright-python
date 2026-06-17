from playwright.sync_api import  Playwright, Page, expect

def test_add_multiple_products_into_cart(page:Page):

    page.goto("https://automationexercise.com/")
    first_product = page.locator(".col-sm-4").nth(1)
    first_product.locator(".productinfo a").click()
    page.get_by_role("button", name="Continue Shopping").click()

    second_product = page.locator(".col-sm-4").nth(4)
    second_product.locator(".productinfo a").click(force=True)
    page.locator(".modal-content a[href='/view_cart']").click()

    expect(page.locator("#cart_info_table tbody tr")).to_have_count(2)

def test_product_quantity_in_cart(page:Page):
    page.goto("https://automationexercise.com/")
    product = page.locator(".col-sm-4").nth(1)
    product.locator("a[href='/product_details/1']").click()
    page.locator("input[name='quantity']").fill("3")
    page.get_by_role("button", name="Add to cart").click()
    page.locator(".modal-body a[href='/view_cart']").click()
    expect(page.get_by_role("button", name="3")).to_be_visible()

def test_remove_product_from_cart(page:Page):

    page.goto("https://automationexercise.com/")
    first_product = page.locator(".col-sm-4").nth(1)
    first_product.locator(".productinfo a").click()
    page.get_by_role("button", name="Continue Shopping").click()

    second_product = page.locator(".col-sm-4").nth(4)
    second_product.locator(".productinfo a").click(force=True)
    page.locator(".modal-content a[href='/view_cart']").click()

    page.locator(".cart_delete a.cart_quantity_delete").first.click()
    expect(page.locator("#cart_info_table tbody tr")).to_have_count(1)

