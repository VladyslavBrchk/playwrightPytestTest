from playwright.sync_api import Page
import random
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.test_data import Data
from faker import Faker


class Helper:
    def __init__(self, page: Page):
        self.page = page
        self.login_page = LoginPage(self.page)
        self.home_page = HomePage(self.page)

    def create_user(self, options) -> None:
        self.login_page = LoginPage(self.page)
        self.home_page = HomePage(self.page)
        self.home_page.click_signup_login_btn()
        self.login_page.sign_up(options[0], options[1])
        self.login_page.enter_account_info(options[2], options[3], options[4], options[5], options[6])
        self.login_page.enter_address_info(options[7], options[8], options[9], options[10], options[11], options[12],
                                           options[13], options[14], options[15])
        self.login_page.click_continue_btn()
        self.home_page.click_logout_btn()

    def create_fake_user(self):
        fake = Faker()
        username = fake.name()
        email = fake.email()
        password = fake.password()
        first_name = fake.first_name()
        last_name = fake.last_name()
        company = fake.company()
        address = fake.address()
        country = Data.countries[random.randint(0, 6)]
        state = fake.state()
        city = fake.city()
        zipcode = fake.zipcode()
        mobile_number = fake.phone_number()
        days = str(random.randint(1, 31))
        months = str(random.randint(1, 12))
        years = str(random.randint(1900, 2021))
        gender = str(random.randint(1, 2))
        options = [username, email, gender, password, days, months, years, first_name, last_name, company, address, country,
                   state, city, zipcode, mobile_number]
        self.create_user(options)
        return options
