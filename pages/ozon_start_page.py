from locators.ozon_start_page_locators import OzonPageLocators
from pages.base_page import BasePage


class OzonStartPage(BasePage):
    locators = OzonPageLocators()

    def check(self):
        x = self.element_is_presence(self.locators.CATALOG)
        x.click()
