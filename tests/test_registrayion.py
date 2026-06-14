from playwright.sync_api import  Playwright, Page, expect
import re


def test_register_user(page:Page):
    page.goto("https://automationexercise.com/")

    # Verify homepage is loaded successfully
    expect(page).to_have_title("Automation Exercise")
    expect(page.locator(".title", has_text="Features Items")).to_be_visible()

    # test Signup
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    expect(page.get_by_text("New User Signup!")).to_be_visible()

    page.get_by_placeholder("Name").fill("Adel")
    page.locator("[data-qa='signup-email']").fill("adel.elakour@gmail.com")
    page.locator("[data-qa='signup-button']").click()

    expect(page).to_have_title("Automation Exercise - Signup")

    # #fill registration data
    page.locator("#id_gender1").check()
    # page.get_by_role("radio", name="Mr.").check()
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

def test_login_correct_credential(page: Page):
    #open login/registration page
    page.goto("https://automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")
    expect(page.locator(".title", has_text="Features Items")).to_be_visible()

    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    expect(page.get_by_text("New User Signup!")).to_be_visible()

    # test Login with correct credentials
    page.locator("input[data-qa=login-email]").fill("adel.elakour@gmail.com")
    page.locator("input[data-qa=login-password]").fill("123456789")
    page.get_by_role("button", name="Login").click()

def test_logout(page: Page):

    #open login/registration page
    page.goto("https://automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")
    expect(page.locator(".title", has_text="Features Items")).to_be_visible()

    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    expect(page.get_by_text("New User Signup!")).to_be_visible()

    # test Login with correct credentials
    page.locator("input[data-qa=login-email]").fill("adel.elakour@gmail.com")
    page.locator("input[data-qa=login-password]").fill("123456789")
    page.get_by_role("button", name="Login").click()

    # logout
    page.get_by_role("link", name="Logout").click()

    # test Login with correct credentials
    page.locator("input[data-qa=login-email]").fill("adel.elakour@gmail.com")
    page.locator("input[data-qa=login-password]").fill("123456789")
    page.get_by_role("button", name="Login").click()

    #logout

def test_login_incorrect_credential(page: Page):
    #open login/registration page
    page.goto("https://automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")
    expect(page.locator(".title", has_text="Features Items")).to_be_visible()

    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    expect(page.get_by_text("New User Signup!")).to_be_visible()

    # test Login with correct credentials
    page.locator("input[data-qa=login-email]").fill("adel.dodo@gmail.com")
    page.locator("input[data-qa=login-password]").fill("2547869")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Your email or password is incorrect")).to_be_visible()

def test_delete_account(page: Page):
    # open login/registration page
    page.goto("https://automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")
    expect(page.locator(".title", has_text="Features Items")).to_be_visible()

    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    expect(page.get_by_text("New User Signup!")).to_be_visible()

    # test Login with correct credentials
    page.locator("input[data-qa=login-email]").fill("adel.elakour@gmail.com")
    page.locator("input[data-qa=login-password]").fill("123456789")
    page.get_by_role("button", name="Login").click()

    # delete account
    page.get_by_role("link", name="Delete Account").click()
    expect(page.get_by_text("Account Deleted")).to_be_visible()
