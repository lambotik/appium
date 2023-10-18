import time

from appium.webdriver.common.appiumby import AppiumBy

from locators.ozon_start_page_locators import OzonPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class OzonStartPage(BasePage):
    locators = OzonPageLocators()
    SEARCH = (AppiumBy.ID, 'ru.ozon.app.android:id/searchTv')

    def check(self):
        x = self.element_is_presence(self.locators.CATALOG)
        x.click()

    # def check2(self):
    #     self.double_click(self.locators.search2)

