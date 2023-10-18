from pages.ozon_start_page import OzonStartPage


class TestOzonMarket:
    def test_click_catalog(self, driver):
        start_page = OzonStartPage(driver)
        start_page.check()

