from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_PRODUCT = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ALERT_SUCCESS = (By.CSS_SELECTOR, '.alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_COST = (By.CSS_SELECTOR, '.product_main .price_color')
    COST_BASKET_IN_ALERT = (By.CSS_SELECTOR, '.alertinner p strong')
