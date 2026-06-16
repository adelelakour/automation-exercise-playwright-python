from playwright.sync_api import Page, expect
import pytest
import random

def user_registration(page:Page):
    page.goto("https://automationexercise.com/")

    # Verify homepage is loaded successfully
    expect(page).to_have_title("Automation Exercise")
    expect(page.locator(".title", has_text="Features Items")).to_be_visible()

    # Test Signup page
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    expect(page.get_by_text("New User Signup!")).to_be_visible()

    # insert preliminary data
    page.get_by_placeholder("Name").fill("Adel")
    rand_num = random.randint(1,10000)
    page.locator("[data-qa='signup-email']").fill(f"adel.elakour{rand_num}@gmail.com")
    page.locator("[data-qa='signup-button']").click()
    expect(page).to_have_title("Automation Exercise - Signup")

    # fill registration data
    page.locator("#id_gender1").check()
    page.locator("input[data-qa='name']").fill("Adel")
    page.locator("input[data-qa='password']").fill("123456789")
    page.locator("[data-qa='days']").select_option("21")
    page.locator("[data-qa='months']").select_option("August")
    page.locator("[data-qa='years']").select_option("1992")
    page.locator("input[data-qa='first_name']").fill("Adel")
    page.locator("input[data-qa='last_name']").fill("Elakour")
    page.locator("input[data-qa='company']").fill("Adel")
    page.locator("input[data-qa=address]").fill("Felsennelkenanger 11")
    page.locator(page.locator("[data-qa='address']"))
    page.get_by_label("Country").select_option("Canada")
    page.locator("input[data-qa=state]").fill("Ontario")
    page.locator("input[data-qa=state]").fill("Ontario")
    page.locator("input[data-qa=city]").fill("Toronto")
    page.locator("input[data-qa=zipcode]").fill("80937")
    page.locator("input[data-qa=mobile_number]").fill("01778414899")
    page.get_by_role("button", name="Create Account").click()
    expect(page.get_by_text("Account Created")).to_be_visible()
    page.get_by_role("link", name="Continue").click()

    return page

def add_multiple_items(page:Page):
    page.goto("https://automationexercise.com/")
    first_product = page.locator(".col-sm-4").nth(1)
    first_product.locator(".productinfo a").click()
    page.get_by_role("button", name="Continue Shopping").click()
    second_product = page.locator(".col-sm-4").nth(4)
    second_product.locator(".productinfo a").click(force=True)
    page.locator(".modal-content a[href='/view_cart']").click()
    expect(page.locator("#cart_info_table tbody tr")).to_have_count(2)
    return page

def remove_item(page:Page):
    page.locator(".cart_delete a.cart_quantity_delete").first.click()
    expect(page.locator("#cart_info_table tbody tr")).to_have_count(1)
    return page

def payment_process(page:Page):
    page.locator("a.check_out").click()
    page.get_by_role("link", name="Place Order").click()
    page.locator("input[name='name_on_card']").fill("Adel Elakour")
    page.locator("input[name='card_number']").fill("2365478901")
    page.locator("input[name='cvc']").fill("333")
    page.locator("input[name='expiry_month']").fill("08")
    page.locator("input[name='expiry_year']").fill("2030")
    page.get_by_role("button", name="Pay and Confirm Order").click()

