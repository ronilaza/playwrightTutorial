from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.mark.regression
def test_login(set_up) -> None:
    page = set_up

    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill("test123")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()

    expect(page.get_by_text("500 Terry Francois Street San Francisco, CA 94158")).to_be_visible()

