from pages.ozon_start_page import OzonStartPage


class TestOzonMarket:
    def test_click_catalog(self, driver):
        start_page = OzonStartPage(driver)
        start_page.check()

    # def test_something(self, driver):
    #     start_page = OzonStartPage(driver)
    #     print(start_page.get_settings())