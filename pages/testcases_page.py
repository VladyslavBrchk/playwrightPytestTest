from playwright.sync_api import Page


class CasesPage:
    def __init__(self, page: Page):
        self.page = page

    def check_url(self) -> None:
        if "/#google_vignette" in self.page.url:
            frame = self.page.frame_locator('#aswift_6').frame_locator('#ad_iframe').get_by_text("Close")
            if frame.is_visible():
                frame.click()
        assert self.page.url == 'https://automationexercise.com/test_cases', \
            f'Expected https://automationexercise.com/test_cases , got "{self.page.url}" instead'
