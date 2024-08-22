import pytest

def test_search_functionality(amazon_ui_app):
    amazon_ui_app.navigate("https://www.amazon.com")
    amazon_ui_app.home_page.search_product("Book")
    search_results = amazon_ui_app.home_page.get_search_results()
    assert len(search_results) > 0, "No results found for 'Book'"



def test_home_page_title(amazon_ui_app):
    amazon_ui_app.navigate("https://www.amazon.com")
    title = amazon_ui_app.get_title()
    assert title == "Amazon.com", "Home page title does not match."
