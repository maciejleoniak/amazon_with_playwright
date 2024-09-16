import pytest
from playwright.sync_api import sync_playwright

from src.application.ui.amazon_ui import AmazonUI


def pytest_html_report_title(report):
    report.title = "Amazon with Playwright"


@pytest.fixture
def amazon_ui_app():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        amazonui_app = AmazonUI(page=page)
        amazonui_app.open()

        yield amazonui_app

        context.close()
        browser.close()
