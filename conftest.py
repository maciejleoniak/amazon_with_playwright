import pytest
from src.application.ui.amazon_ui import AmazonUI
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='session')
def amazon_ui_app():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        app = AmazonUI(page)
        yield app
        browser.close()
