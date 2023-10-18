import os

import pytest
from appium import webdriver

"""from appium.options.common import AppiumOptions"""
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

ANDROID_APP_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../app')

apk_files = [f for f in os.listdir(ANDROID_APP_DIR) if f.endswith('.apk')]
assert len(apk_files) == 1, 'App directory can only contain one app file.'
ANDROID_APP_PATH = os.path.join(ANDROID_APP_DIR, apk_files.pop(0))

cap = {
    "platformName": 'Android',
    "automationName": 'UiAutomator2',
    "deviceName": 'Andorid',
    "appActivity": 'ru.ozon.app.android.ui.start.PreStartActivity',
    "app": rf'{ANDROID_APP_PATH}',
    "language": 'ru',
    "locale": 'RU'
}
# capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
url = 'http://localhost:4723'


@pytest.fixture()
def driver():
    driver = webdriver.Remote(url, options=UiAutomator2Options().load_capabilities(cap))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


"""First test"""


def test_1(driver):
    ozon_page = driver
    try:
        ozon_page.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='HandlerView')
        ozon_page.back()
    except Exception as ex:
        print(ex)
    # ozon_page.swipe(start_y=1020, start_x=500, end_y=1700, end_x=500)

    ozon_page.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Главная').click()
    catalog = ozon_page.find_element(by=AppiumBy.XPATH,
                                     value='//android.view.ViewGroup[@content-desc="Каталог"]'
                                           '/android.widget.ImageView')
    catalog.click()
    search = ozon_page.find_element(by=AppiumBy.ID, value='ru.ozon.app.android:id/searchTv')
    search.click()
    ozon_page.find_element(by=AppiumBy.ID, value='ru.ozon.app.android:id/searchEt').send_keys('мяч')
    ozon_page.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup'
                                                    '[@content-desc="мяч футбольный"]/android.widget.TextView').click()
    ozon_page.find_element(by=AppiumBy.XPATH, value='(//android.widget.FrameLayout[@content-desc="grid"])'
                                                    '[1]/android.view.ViewGroup/android.widget.FrameLayout').click()

    ozon_page.find_element(by=AppiumBy.ID, value='ru.ozon.app.android:id/btnTitleTv')
    ozon_page.swipe(start_y=1400, start_x=500, end_y=700, end_x=500)

    price = ozon_page.find_element(by=AppiumBy.XPATH,
                                   value='//android.view.ViewGroup[@content-desc="21,47 BYN"]'
                                         '/android.widget.TextView[1]').text
    print(price)
    ozon_page.find_element(by=AppiumBy.ID, value='ru.ozon.app.android:id/btnTitleTv').click()
    inbox = ozon_page.find_element(by=AppiumBy.ID, value='ru.ozon.app.android:id/btnTitleTv')
    assert inbox.text == 'В корзине'

    ozon_page.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Корзина"]'
                                                    '/android.widget.ImageView').click()
    price_in_cart = ozon_page.find_element(by=AppiumBy.ID, value='ru.ozon.app.android:id/totalStickyInfoText').text
    print(price_in_cart)
    assert price == price_in_cart
