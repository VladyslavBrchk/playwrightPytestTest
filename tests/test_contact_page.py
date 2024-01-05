import pytest
from pages.home_page import HomePage
from pages.contact_page import ContactPage
from utils.tools import take_screenshot
from faker import Faker


class TestContact:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.contact_page = ContactPage(self.page)
        self.home_page.check_home_page_visible()

    def test_contact_us(self, test_setup):
        fake = Faker()
        name = fake.name()
        email = fake.email()
        subject = fake.sentence()
        message = fake.paragraph()
        self.home_page.click_contact_us_btn()
        self.contact_page.check_contact_form_title()
        self.contact_page.fill_contact_us_form(name, email, subject, message)
        self.contact_page.click_contact_form_submit_btn()
        self.contact_page.click_browser_ok()
        self.contact_page.click_contact_form_submit_btn()
        self.contact_page.check_success_msg()
        self.contact_page.click_success_back_home_btn()
        self.home_page.check_url()
        take_screenshot(self.page, "contact_us")

