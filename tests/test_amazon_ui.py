def test_home_page_title(amazon_ui_app):
    amazon_ui_app.amazon_home_page.navigate_to()
    title = amazon_ui_app.get_title()
    assert (
        title == "Amazon.com. Spend less. Smile more."
    ), "Home page title does not match."


# def test_search_functionality(amazon_ui_app):
#     amazon_ui_app.amazon_home_page.search_product("Book")
#     search_results = amazon_ui_app.amazon_home_page.get_search_results()
#     assert len(search_results) > 0, "No results found for 'Book'"
