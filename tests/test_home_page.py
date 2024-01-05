import pytest
from pages.home_page import HomePage
from utils.tools import take_screenshot
from faker import Faker


class TestHome:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.home_page.check_home_page_visible()

    def test_subscription(self, test_setup):
        fake = Faker()
        self.home_page.scroll_down()
        self.home_page.check_subscription()
        self.home_page.subscribe(fake.email())
        self.home_page.check_subscription_msg()
        take_screenshot(self.page, "subscription")
