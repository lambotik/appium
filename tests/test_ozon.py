import time

from pages.ozon_start_page import OzonStartPage


class TestOzonMarket:
    def test_click_catalog(self, driver):
        session_id = driver.session_id
        print(session_id)
        start_page = OzonStartPage(driver)
        price_market, price_in_cart = start_page.check()
        assert price_market == price_in_cart, 'Critical bag!!!'
