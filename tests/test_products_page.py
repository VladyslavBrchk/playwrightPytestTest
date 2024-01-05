import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from utils.tools import take_screenshot


class TestProducts:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.products_page = ProductsPage(self.page)
        self.home_page.check_home_page_visible()
        self.home_page.click_products_btn()
        self.products_page.check_url()

    def test_products_page(self, test_setup):
        self.products_page.check_products_list_visible()
        self.products_page.view_products_item(1)
        self.products_page.check_products_item_url(1)
        self.products_page.products_item_details_visible()
        take_screenshot(self.page, "products page")

    def test_search_product(self, test_setup):
        self.products_page.search_product('Green')
        self.products_page.check_search_results('Green')
        take_screenshot(self.page, "search product")
