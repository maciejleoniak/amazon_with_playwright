from playwright.sync_api import Page

from src.application.ui.base_app import BaseApp


class HomePage(BaseApp):
    URL = "https://amazon.com"

    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate_to(self):
        self.page.goto(self.URL)

    def search_product(self, product_name: str):
        self.page.fill("input[name='field-keywords']", product_name)
        self.page.click("input#nav-search-submit-button")

    def get_search_results(self):
        return self.page.query_selector_all(
            "span.a-size-medium.a-color-base.a-text-normal"
        )
