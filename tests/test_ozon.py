from pprint import pprint

from pages.ozon_start_page import OzonStartPage


class TestOzonMarket:
    def test_click_catalog(self, driver):
        session_id = driver.session_id
        print(session_id)
        start_page = OzonStartPage(driver)
        price_market, price_in_cart = start_page.check()
        assert price_market == price_in_cart, 'Critical bag!!!'

    def test_get_settings(self,driver):
        """
        This method gets device info
        :param driver:
        :return:
        """
        settings = driver.get_settings()
        battery_info = driver.battery_info
        capabilities = driver.capabilities
        device_time = driver.device_time
        print('Battery_info:', battery_info)
        print('\nCapabilities:')
        pprint(capabilities)
        print('\ndevice_time',device_time)
        print('\nsettings')
        pprint(settings)
