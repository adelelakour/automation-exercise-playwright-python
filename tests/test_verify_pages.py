from playwright.sync_api import  Playwright, Page, expect
import re

def test_verify_test_cases_page(page:Page):
    page.goto("https://automationexercise.com/")
    page.get_by_role("link", name="Test Cases").first.click()
    expect(page.get_by_text("Below is the list of test Cases")).to_be_visible()

def test_verify_test_cases_page(page:Page):
    page.goto("https://automationexercise.com/")
    expect(page.get_by_text("Features Items")).to_be_visible()
    page.get_by_role("link", name="Products").click()
    expect(page.get_by_text("All Products")).to_be_visible()
    page.get_by_role("link", name="View Product").first.click()
    expect(page.get_by_text("Quantity")).to_be_visible()
    expect(page.get_by_text("Condition")).to_be_visible()
    expect(page.get_by_text("Brand:")).to_be_visible()
    expect(page.get_by_text("Availability:")).to_be_visible()

def test_verify_test_cases_page(page:Page):
    page.goto("https://automationexercise.com/")
    expect(page.get_by_text("Features Items")).to_be_visible()
    page.get_by_role("link", name="Products").click()
    expect(page.get_by_text("All Products")).to_be_visible()
    page.get_by_placeholder("Search Product").fill("Top for women")
    page.locator("#submit_search").click()
    expect(page.get_by_text("Searched Products")).to_be_visible()

