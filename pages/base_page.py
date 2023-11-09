from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as Wait


class BasePage(WebDriver):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def element_is_presence(self, locator):
        return Wait(self.driver, self.timeout).until(ec.presence_of_element_located(locator),
                                                     message=f'Element not found by locator: {locator}')
