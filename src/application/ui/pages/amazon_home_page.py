class HomePage:

    URL = "https://amazon.com"
    SEARCH_BTN = "input[name='field-keywords']"

    def __init__(self, page) -> None:
        self.page = page

    def navigate_to(self):
        self.page.goto(self.URL)

    def search_product(self, product_name: str):
        self.page.search_product(self.SEARCH_BTN, product_name)

    # def get_search_results(self):
    #     return self.page.query_selector_all(
    #         "span.a-size-medium.a-color-base.a-text-normal"
    #     )
