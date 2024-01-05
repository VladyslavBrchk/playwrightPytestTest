import pytest
from pages.home_page import HomePage
from pages.testcases_page import CasesPage
from utils.tools import take_screenshot


class TestCases:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.testcases_page = CasesPage(self.page)
        self.home_page.check_home_page_visible()

    def test_testcases_page(self, test_setup):
        self.home_page.click_testcases_btn()
        self.testcases_page.check_url()
        take_screenshot(self.page, "testcases page")
