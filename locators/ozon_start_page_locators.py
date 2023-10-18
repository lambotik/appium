
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


class OzonPageLocators:
    search = (AppiumBy.ACCESSIBILITY_ID, 'ru.ozon.app.android:id/searchTv')
    HANDLER_VIEW = (AppiumBy.ACCESSIBILITY_ID, 'HandlerView')
    MAIN = (AppiumBy.ACCESSIBILITY_ID, 'Главная')
    CATALOG = (AppiumBy.ACCESSIBILITY_ID, "Каталог")


