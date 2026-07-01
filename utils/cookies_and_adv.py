from playwright.sync_api import Page, expect
from playwright.sync_api import TimeoutError


def accept_cookies(page: Page):
    buttons = [
        "Accept",
        "Close",
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



def register_cookie_handler(page: Page):
    def accept_cookie_banner():
        page.get_by_role("button", name="Consent").click()

    page.add_locator_handler(
        page.get_by_role("button", name="Consent"),
        accept_cookie_banner
    )


def close_ad_if_visible(page: Page):
    for frame in page.frames:
        try:
            frame.get_by_role("button", name="Close").click(timeout=1000)
            return True
        except TimeoutError:
            pass

    return False