from playwright.sync_api import  Playwright, Page, expect


def test_place_order_logged_in_user(page:Page, login, payment):
    product = login.locator(".col-sm-4").nth(4)
    product.locator(".productinfo a").click(force=True)
    login.locator(".modal-content a[href='/view_cart']").click()
    login.locator("a.check_out").click()
    login.get_by_role("link", name="Place Order").click()
    payment(login)
    login.get_by_role("button", name="Pay and Confirm Order").click()
