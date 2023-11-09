from appium.webdriver.common.appiumby import AppiumBy


class OzonPageLocators:
    search = (AppiumBy.ID, 'ru.ozon.app.android:id/searchTv')
    HANDLER_VIEW = (AppiumBy.ACCESSIBILITY_ID, 'HandlerView')
    MAIN = (AppiumBy.ACCESSIBILITY_ID, 'Главная')
    CATALOG = (AppiumBy.ACCESSIBILITY_ID, "Каталог")
    ADVERTISING = (AppiumBy.ID, 'ru.ozon.app.android:id/touch_outside')
    LATER = (AppiumBy.ID, 'ru.ozon.app.android:id/remindLater')
    FRAME = (AppiumBy.ID, 'ru.ozon.app.android:id/design_bottom_sheet')
    BALL = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="мяч футбольный"]/android.widget.TextView')
    CATALOG_SEARCH = (AppiumBy.ID, 'ru.ozon.app.android:id/searchEt')
    SELECT_BALL = (AppiumBy.XPATH,
                   '(//android.widget.FrameLayout[@content-desc="grid"])[1]'
                   '/android.view.ViewGroup/android.widget.FrameLayout')
    PRICE = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="25,20 BYN"]/android.widget.TextView')
    TITLE = (AppiumBy.ID, 'ru.ozon.app.android:id/btnTitleTv')
    CART = (AppiumBy.ID, 'ru.ozon.app.android:id/cartBtn')
    BADGE = (AppiumBy.ID, 'ru.ozon.app.android:id/tab_badge')
    GO_IN_CART = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Корзина"]/android.widget.ImageView')
    PRICE_IN_CART = (AppiumBy.ID, 'ru.ozon.app.android:id/footerPriceTv')
