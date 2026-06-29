from playwright.sync_api import Page, expect
from playwright.sync_api import TimeoutError


def accept_cookies(page: Page):
    buttons = [
        "Accept",
        "Consent",
        "Accept All",
        "Accept all",
        "Allow all",
        "I agree",
        "Agree",
        "OK",
        "Got it",
        "Accept cookies",
        "Alle akzeptieren",
        "Alle akzeptieren & schließen",
        "Akzeptieren",
        "Zustimmen",
    ]

    for text in buttons:
        try:
            page.get_by_role("button", name=text, exact=False).click(timeout=500)
            return
        except TimeoutError:
            pass
        except Exception:
            pass
