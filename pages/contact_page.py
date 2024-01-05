from playwright.sync_api import Page


class ContactPage:
    def __init__(self, page: Page):
        self.page = page
        self.__contact_form_title = self.page.locator('.contact-form > h2')
        self.__contact_form_name_input = self.page.locator('[data-qa="name"]')
        self.__contact_form_email_input = self.page.locator('[data-qa="email"]')
        self.__contact_form_subject_input = self.page.locator('[data-qa="subject"]')
        self.__contact_form_message_input = self.page.locator('[data-qa="message"]')
        self.__contact_form_upload_btn = self.page.locator('[name="upload_file"]')
        self.__contact_form_submit_btn = self.page.locator('[data-qa="submit-button"]')
        self.__success_msg = self.page.locator('.status')
        self.__success_back_home_btn = self.page.locator('.btn-success')

    def check_contact_form_title(self) -> None:
        self.__contact_form_title.wait_for(state='visible')
        assert self.__contact_form_title.text_content() == 'Get In Touch', \
            f'Expected Get In Touch , got "{self.__contact_form_title.text_content()}" instead'

    def fill_contact_us_form(self, name, email, subject, message) -> None:
        self.__contact_form_name_input.fill(name)
        self.__contact_form_email_input.fill(email)
        self.__contact_form_subject_input.fill(subject)
        self.__contact_form_message_input.fill(message)
        with self.page.expect_file_chooser() as fc_info:
            self.__contact_form_upload_btn.click()
        file_chooser = fc_info.value
        file_chooser.set_files('data/image.jpg')

    def click_contact_form_submit_btn(self) -> None:
        self.__contact_form_submit_btn.click()

    def click_browser_ok(self) -> None:
        self.page.on("dialog", lambda dialog: dialog.accept())

    def check_success_msg(self) -> None:
        self.__success_msg.wait_for(state='visible')
        assert self.__success_msg.text_content() == 'Success! Your details have been submitted successfully.', \
            f'Expected Success! Your details have been submitted successfully. , got "{self.__success_msg.text_content()}" instead'

    def click_success_back_home_btn(self) -> None:
        self.__success_back_home_btn.click()
