from playwright.sync_api import  Playwright, Page, expect
import re
from pathlib import Path

def test_contact_form(page:Page):
    page.goto("https://automationexercise.com/")
    page.get_by_role("link", name="Contact us").click()
    page.get_by_placeholder("Name").fill("Adel Elakour")
    page.get_by_placeholder("Email", exact=True).fill("adel.elakour@gmail.com")
    page.get_by_placeholder("Subject").fill("Refund request")
    page.get_by_placeholder("Your Message Here").fill("I ordered a t-shirt within order number AD323A and bla bla ")
    file_input = page.locator("input[name='upload_file']")

    project_root = Path(__file__).resolve().parents[1]
    image_path = project_root / "images" / "shirt.jpg"

    page.locator("input[name='upload_file']").set_input_files(str(image_path))


    file_input = page.locator("input[name='submit']").click()
    page.on("dialog", lambda dialog: dialog.accept())
    