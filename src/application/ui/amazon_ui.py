from src.application.ui.pages.amazon_home_page import HomePage
from src.application.ui.base_app import BaseApp

class AmazonUI(BaseApp):
    def __init__(self, page):
        super().__init__(page)
        self.home_page = HomePage(page)
