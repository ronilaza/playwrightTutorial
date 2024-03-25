from playwright.sync_api import playwright
import pytest

@pytest.fixture
def set_up(page):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()

    # # open a new page
    # page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")

    yield page
