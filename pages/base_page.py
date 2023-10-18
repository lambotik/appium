from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait as wait, WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# check
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.touch_action import TouchAction


class BasePage(WebDriver):
    def __init__(self, driver):
        # super().__init__()
        self.driver = driver
        self.timeout = 10

    def element_is_presence(self, locator):
        return wait(self.driver, self.timeout).until(ec.presence_of_element_located(locator))

    def x(self):
        pass
