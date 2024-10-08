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
