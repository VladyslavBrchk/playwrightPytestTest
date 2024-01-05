from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.__page_body = self.page.locator('body')
        self.__signup_login_btn = self.page.locator('li > [href="/login"]')
        self.__logged_as = self.page.locator('.navbar-nav > li:last-child')
        self.__delete_account_btn = self.page.locator('[href="/delete_account"]')
        self.__account_deleted_msg = self.page.locator('[data-qa="account-deleted"]')
        self.__logout_btn = self.page.locator('li > [href="/logout"]')
        self.__continue_btn = self.page.locator('[data-qa="continue-button"]')
        self.__contact_us_btn = self.page.locator('li > [href="/contact_us"]')
        self.__testcases_btn = self.page.locator('li > [href="/test_cases"]')
        self.__products_btn = self.page.locator('li > [href="/products"]')
        self.__footer_subscription = self.page.locator('.single-widget > h2')
        self.__footer_subscription_email_input = self.page.locator('#susbscribe_email')
        self.__footer_subscription_submit_btn = self.page.locator('#subscribe')
        self.__success_subscription_msg = self.page.locator('#success-subscribe')

    def check_home_page_visible(self) -> None:
        assert self.__page_body.is_visible(), "Home Page is not visible"

    def click_signup_login_btn(self) -> None:
        self.__signup_login_btn.click()

    def check_logged_as_msg(self, username) -> None:
        self.__logged_as.wait_for(state='visible')
        assert self.__logged_as.text_content() == ' Logged in as ' + username, \
            f'Expected Logged in as username , got "{self.__logged_as.text_content()}" instead'

    def click_delete_account_btn(self) -> None:
        self.__delete_account_btn.click()

    def check_account_deleted_msg(self) -> None:
        self.__account_deleted_msg.wait_for(state='visible')
        assert self.__account_deleted_msg.text_content() == 'Account Deleted!', \
            f'Expected Account Deleted! , got "{self.__account_deleted_msg.text_content()}" instead'

    def click_logout_btn(self) -> None:
        self.__logout_btn.click()

    def click_continue_btn(self) -> None:
        self.__continue_btn.click()

    def click_contact_us_btn(self) -> None:
        self.__contact_us_btn.click()

    def check_url(self) -> None:
        if "/#google_vignette" in self.page.url:
            frame = self.page.frame_locator('#aswift_6').frame_locator('#ad_iframe').get_by_text("Close")
            if frame.is_visible():
                frame.click()
        assert self.page.url == 'https://automationexercise.com/', \
            f'Expected https://automationexercise.com/ , got "{self.page.url}" instead'

    def click_testcases_btn(self) -> None:
        self.__testcases_btn.click()

    def click_products_btn(self) -> None:
        self.__products_btn.click()

    def scroll_down(self) -> None:
        self.page.mouse.wheel(0, 10000)

    def check_subscription(self) -> None:
        assert self.__footer_subscription.text_content() == 'Subscription', \
            f'Expected Subscription , got "{self.__footer_subscription.text_content()}" instead'

    def subscribe(self, email) -> None:
        self.__footer_subscription_email_input.fill(email)
        self.__footer_subscription_submit_btn.click()

    def check_subscription_msg(self) -> None:
        self.__success_subscription_msg.wait_for(state='visible')
        assert 'You have been successfully subscribed!' in self.__success_subscription_msg.text_content(), \
            f'Expected You have been successfully subscribed! , got "{self.__success_subscription_msg.text_content()}" instead'
