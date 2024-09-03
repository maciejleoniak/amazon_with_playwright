from playwright.sync_api import Page

from src.application.ui.base_app import BaseApp
from src.application.ui.pages.amazon_home_page import HomePage


class AmazonUI(BaseApp):
    def __init__(self, page: Page):
        super().__init__(page)
        self.amazon_home_page = HomePage(page)

    def open(self):
        self.amazon_home_page.navigate_to()
