from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as wait


class BasePage(WebDriver):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def element_is_presence(self, locator):
        return wait(self.driver, self.timeout).until(ec.presence_of_element_located(locator))
