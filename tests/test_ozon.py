from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from locators.ozon_start_page_locators import OzonPageLocators
from pages.ozon_start_page import OzonStartPage


class TestOzonMarket:
    def test_work(self, driver):
        page = driver
        wait = WebDriverWait(driver, 10)
        x = wait.until(ec.presence_of_element_located(OzonPageLocators.CATALOG))
        x.click()

    def test_dont_work(self, driver):
        # page = driver
        # wait = WebDriverWait(driver, 10)
        # x = wait.until(ec.presence_of_element_located(OzonPageLocators.CATALOG))
        start_page = OzonStartPage(driver)
        start_page.check()

