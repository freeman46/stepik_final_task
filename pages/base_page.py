from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException, \
    InvalidSelectorException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math


class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Вспомогательный метод (ищет элемент и кликает по нему)
    def find_button_and_click(self, how, what):
        assert self.is_element_present(how, what), f'Элемент "{what}" не найден!'
        button = self.browser.find_element(how, what)
        button.click()

    # Вспомогательный метод (ищет элемент и берет текст элемента)
    def find_element_and_get_text(self, how, what):
        assert self.is_element_present(how, what), f'Элемент "{what}" не найден!'
        element = self.browser.find_element(how, what)
        return element.text

    # Вспомогательный метод (ищет элемент, очищает поле ввода, вводит текст)
    def find_element_and_input_text(self, how, what, text):
        assert self.is_element_present(how, what), f'Поле "{what}" не найдено!'
        input_field = self.browser.find_element(how, what)
        input_field.clear()
        input_field.send_keys(text)

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_elements(how, what)
        except (NoSuchElementException, InvalidSelectorException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
