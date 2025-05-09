# tests/test_home.py
from pages.home_page import HomePage

def test_home_page_title(logged_in_browser):
    home_page = HomePage(logged_in_browser)
    home_page.open()
    assert "Dashboard" in home_page.get_title()
