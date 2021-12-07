from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert '/login/' in self.browser.current_url, 'Некорректный URL страницы логина'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Отсутствует форма для логина пользователя'

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), 'Отсутствует форма для регистарции пользователя'

    def register_new_user(self, email, password):
        self.should_be_register_form()
        self.find_element_and_input_text(*LoginPageLocators.REGISTER_EMAIL_INPUT, email)
        self.find_element_and_input_text(*LoginPageLocators.REGISTER_PASSWORD_INPUT, password)
        self.find_element_and_input_text(*LoginPageLocators.REGISTER_RETRY_PASSWORD_INPUT, password)
        self.find_button_and_click(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
