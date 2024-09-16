from playwright.sync_api import Page


class BaseApp:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def screenshot(self, path: str):
        self.page.screenshot(path=path)

    def search_product(self, locators, product_name: str):
        self.page.fill(locators, product_name)
        self.page.click("input#nav-search-submit-button")

    def get_search_results(self):
        return self.page.query_selector_all(
            "span.a-size-medium.a-color-base.a-text-normal"
        )
