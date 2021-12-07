from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_RETRY_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_SUBMIT_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators():
    ADD_PRODUCT = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ALERT_SUCCESS = (By.CSS_SELECTOR, '.alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_COST = (By.CSS_SELECTOR, '.product_main .price_color')
    COST_BASKET_IN_ALERT = (By.CSS_SELECTOR, '.alertinner p strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.XPATH, '//a[@class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.basket_summary')
    MESSAGE_OF_EMPTY_BASKET = (By.XPATH, '//*[@id="content_inner"]/p')
