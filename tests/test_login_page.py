import pytest
import random
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.helper import Helper
from utils.test_data import Data
from utils.tools import take_screenshot
from faker import Faker


class TestRegister:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.login_page = LoginPage(self.page)
        self.home_page = HomePage(self.page)
        self.helper = Helper(self.page)
        self.home_page.check_home_page_visible()
        self.home_page.click_signup_login_btn()

    def test_register_user(self, test_setup):
        fake = Faker()
        username = fake.name()
        days = str(random.randint(1, 31))
        months = str(random.randint(1, 12))
        years = str(random.randint(1900, 2021))
        self.login_page.check_signup_form_title()
        self.login_page.sign_up(username, fake.email())
        self.login_page.check_account_info_form_title()
        self.login_page.enter_account_info(2, fake.password(), days, months, years)
        self.login_page.enter_address_info(fake.first_name(), fake.last_name(), fake.company(), fake.address(),
                                           Data.countries[random.randint(0, 6)], fake.state(), fake.city(),
                                           fake.zipcode(), fake.phone_number())
        self.login_page.check_account_created_msg()
        self.login_page.click_continue_btn()
        self.home_page.check_logged_as_msg(username)
        self.home_page.click_delete_account_btn()
        self.home_page.check_account_deleted_msg()
        self.home_page.click_continue_btn()
        take_screenshot(self.page, "register")


class TestLogin:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.login_page = LoginPage(self.page)
        self.home_page = HomePage(self.page)
        self.helper = Helper(self.page)
        global random_options
        random_options = self.helper.create_fake_user()
        self.home_page.check_home_page_visible()
        self.home_page.click_signup_login_btn()

    def test_valid_login(self, test_setup):
        username = random_options[0]
        email = random_options[1]
        password = random_options[3]
        self.login_page.check_login_form_title()
        self.login_page.log_in(email, password)
        self.home_page.check_logged_as_msg(username)
        self.home_page.click_delete_account_btn()
        self.home_page.check_account_deleted_msg()
        self.home_page.click_continue_btn()
        take_screenshot(self.page, "valid login")

    def test_invalid_login(self, test_setup):
        fake = Faker()
        email = fake.email()
        password = fake.password()
        self.login_page.check_login_form_title()
        self.login_page.log_in(email, password)
        self.login_page.check_invalid_login_error_msg()
        take_screenshot(self.page, "invalid login")

    def test_logout(self, test_setup):
        username = random_options[0]
        email = random_options[1]
        password = random_options[3]
        self.login_page.check_login_form_title()
        self.login_page.log_in(email, password)
        self.home_page.check_logged_as_msg(username)
        self.home_page.click_logout_btn()
        self.login_page.check_url()
        take_screenshot(self.page, "logout")

    def test_invalid_signin(self, test_setup):
        username = random_options[0]
        email = random_options[1]
        self.login_page.check_login_form_title()
        self.login_page.sign_up(username, email)
        self.login_page.check_invalid_signup_error_msg()
        take_screenshot(self.page, "invalid sign in")
