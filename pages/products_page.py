from playwright.sync_api import Page


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.__products_list = self.page.locator('.features_items')
        self.__products_item_name = self.page.locator('.product-information > h2')
        self.__products_item_category = self.page.locator('.product-information > p:nth-of-type(1)')
        self.__products_item_price = self.page.locator('.product-information > span > span')
        self.__products_item_availability = self.page.locator('.product-information > p:nth-of-type(2)')
        self.__products_item_condition = self.page.locator('.product-information > p:nth-of-type(3)')
        self.__products_item_brand = self.page.locator('.product-information > p:nth-of-type(4)')
        self.__search_product_input = self.page.locator('#search_product')
        self.__search_product_btn = self.page.locator('#submit_search')
        self.__founded_products_names = self.page.locator('.productinfo > p')

    def check_url(self) -> None:
        if "/#google_vignette" in self.page.url:
            frame = self.page.frame_locator('#aswift_6').frame_locator('#ad_iframe').get_by_text("Close")
            if frame.is_visible():
                frame.click()
        assert self.page.url == 'https://automationexercise.com/products', \
            f'Expected https://automationexercise.com/products , got "{self.page.url}" instead'

    def check_products_list_visible(self) -> None:
        assert self.__products_list.is_visible(), "Products List is not visible"

    def view_products_item(self, index):
        item = self.page.locator(f'[href="/product_details/{index}"]')
        item.click()

    def check_products_item_url(self, index) -> None:
        assert self.page.url == f'https://automationexercise.com/product_details/{index}', \
            f'Expected https://automationexercise.com/product_details/{index} , got "{self.page.url}" instead'

    def products_item_details_visible(self) -> None:
        assert self.__products_item_name.is_visible(), "Products Name is not visible"
        assert self.__products_item_category.is_visible(), "Products Category is not visible"
        assert self.__products_item_price.is_visible(), "Products Price is not visible"
        assert self.__products_item_availability.is_visible(), "Products Availability is not visible"
        assert self.__products_item_condition.is_visible(), "Products Condition is not visible"
        assert self.__products_item_brand.is_visible(), "Products Brand is not visible"

    def search_product(self, product) -> None:
        self.__search_product_input.fill(product)
        self.__search_product_btn.click()

    def check_search_results(self, request) -> None:
        for elem in self.__founded_products_names.all_text_contents():
            assert request in elem
