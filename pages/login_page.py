from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.__signup_title = self.page.locator('.signup-form > h2')
        self.__signup_name_input = self.page.locator('[data-qa="signup-name"]')
        self.__signup_email_input = self.page.locator('[data-qa="signup-email"]')
        self.__signup_submit_btn = self.page.locator('[data-qa="signup-button"]')
        self.__register_info_title = self.page.locator('.login-form > h2')
        self.__register_password_input = self.page.locator('[data-qa="password"]')
        self.__register_birth_day = self.page.locator('#days')
        self.__register_birth_month = self.page.locator('#months')
        self.__register_birth_year = self.page.locator('#years')
        self.__register_newsletter_checkbox = self.page.locator('#newsletter')
        self.__register_optin_checkbox = self.page.locator('#optin')
        self.__create_account_btn = self.page.locator('[data-qa="create-account"]')
        self.__account_created_msg = self.page.locator('[data-qa="account-created"]')
        self.__continue_btn = self.page.locator('[data-qa="continue-button"]')
        self.__login_email_input = self.page.locator('[data-qa="login-email"]')
        self.__login_password_input = self.page.locator('[data-qa="login-password"]')
        self.__login_submit_btn = self.page.locator('[data-qa="login-button"]')
        self.__invalid_login_error_msg = self.page.locator('form[action="/login"] > p')
        self.__invalid_signup_error_msg = self.page.locator('form[action="/signup"] > p')

    def check_signup_form_title(self) -> None:
        self.__signup_title.wait_for(state='visible')
        assert self.__signup_title.text_content() == 'New User Signup!', \
            f'Expected New User Signup! , got "{self.__signup_title.text_content()}" instead'

    def sign_up(self, username, email) -> None:
        self.__signup_name_input.fill(username)
        self.__signup_email_input.fill(email)
        self.__signup_submit_btn.click()

    def check_account_info_form_title(self) -> None:
        self.__register_info_title.wait_for(state='visible')
        assert self.__register_info_title.text_content() == 'Enter Account Information', \
            f'Expected Enter Account Information , got "{self.__register_info_title.text_content()}" instead'

    def title_radio_button_locator(self, gender):
        return self.page.locator(f'#id_gender{gender}')

    def enter_account_info(self, gender, password, day, month, year) -> None:
        self.title_radio_button_locator(gender).check(force=True)
        self.__register_password_input.fill(password)
        self.__register_newsletter_checkbox.check()
        self.__register_optin_checkbox.check()
        self.__register_birth_day.select_option(day)
        self.__register_birth_month.select_option(month)
        self.__register_birth_year.select_option(year)

    def address_info_locator(self, locator):
        return self.page.locator(f'#{locator}')

    def enter_address_info(self, first_name, last_name, company, address1, country, state, city, zipcode, mobile_number) -> None:
        self.address_info_locator("first_name").fill(first_name)
        self.address_info_locator("last_name").fill(last_name)
        self.address_info_locator("company").fill(company)
        self.address_info_locator("address1").fill(address1)
        self.address_info_locator("country").select_option(country)
        self.address_info_locator("state").fill(state)
        self.address_info_locator("city").fill(city)
        self.address_info_locator("zipcode").fill(zipcode)
        self.address_info_locator("mobile_number").fill(mobile_number)
        self.__create_account_btn.click()

    def check_account_created_msg(self) -> None:
        self.__account_created_msg.wait_for(state='visible')
        assert self.__account_created_msg.text_content() == 'Account Created!', \
            f'Expected Account Created! , got "{self.__account_created_msg.text_content()}" instead'

    def click_continue_btn(self) -> None:
        self.__continue_btn.click()

    def check_login_form_title(self) -> None:
        self.__signup_title.wait_for(state='visible')
        assert self.__signup_title.text_content() == 'New User Signup!', \
            f'Expected New User Signup! , got "{self.__signup_title.text_content()}" instead'

    def log_in(self, email, password) -> None:
        self.__login_email_input.fill(email)
        self.__login_password_input.fill(password)
        self.__login_submit_btn.click()

    def check_invalid_login_error_msg(self) -> None:
        self.__invalid_login_error_msg.wait_for(state='visible')
        assert self.__invalid_login_error_msg.text_content() == 'Your email or password is incorrect!', \
            f'Expected Your email or password is incorrect! , got "{self.__invalid_login_error_msg.text_content()}" instead'

    def check_url(self) -> None:
        assert self.page.url == 'https://automationexercise.com/login', \
            f'Expected https://automationexercise.com/login , got "{self.page.url}" instead'

    def check_invalid_signup_error_msg(self) -> None:
        self.__invalid_signup_error_msg.wait_for(state='visible')
        assert self.__invalid_signup_error_msg.text_content() == 'Email Address already exist!', \
            f'Expected Email Address already exist! , got "{self.__invalid_signup_error_msg.text_content()}" instead'
