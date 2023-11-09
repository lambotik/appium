from locators.ozon_start_page_locators import OzonPageLocators
from pages.base_page import BasePage


class OzonStartPage(BasePage):
    locators = OzonPageLocators()

    def check(self):
        self.element_is_presence(self.locators.LATER).click()
        self.element_is_presence(self.locators.FRAME)
        self.driver.back()
        self.element_is_presence(self.locators.CATALOG).click()
        search = self.element_is_presence(self.locators.search)
        search.click()
        self.element_is_presence(self.locators.CATALOG_SEARCH).send_keys('мяч')
        self.element_is_presence(self.locators.BALL).click()
        self.element_is_presence(self.locators.SELECT_BALL).click()
        self.element_is_presence(self.locators.TITLE)
        self.driver.swipe(start_y=1400, start_x=500, end_y=700, end_x=500)
        price = self.element_is_presence(self.locators.PRICE).text
        print('Price on market:', price)
        self.element_is_presence(self.locators.CART).click()
        assert self.element_is_presence(self.locators.BADGE)
        self.element_is_presence(self.locators.GO_IN_CART).click()
        price_in_cart = self.element_is_presence(self.locators.PRICE_IN_CART).text
        print('Price in cart:', price_in_cart)
        return price, price_in_cart
