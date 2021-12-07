from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_in_basket(self):
        self.find_button_and_click(*ProductPageLocators.ADD_PRODUCT)
        self.solve_quiz_and_get_code()

    def should_be_product_page(self):
        self.add_product_in_basket()
        self.should_be_success_message()
        self.should_be_cost_product()

    def should_be_success_message(self):
        product_name_in_alert = self.find_element_and_get_text(*ProductPageLocators.ALERT_SUCCESS)
        product_name_in_card = self.find_element_and_get_text(*ProductPageLocators.PRODUCT_NAME)
        assert product_name_in_alert == product_name_in_card, \
            f'Ожидалось:{product_name_in_card}, Факт:{product_name_in_alert}'

    def should_be_cost_product(self):
        cost_product_in_card = self.find_element_and_get_text(*ProductPageLocators.PRODUCT_COST)
        cost_basket_in_alert = self.find_element_and_get_text(*ProductPageLocators.COST_BASKET_IN_ALERT)
        assert cost_basket_in_alert == cost_product_in_card, \
            f'Ожидаемая цена в корзине:{cost_product_in_card}, Факт:{cost_basket_in_alert}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS), \
            "Success message is presented, but should not be"

    def should_not_be_present_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS), \
            "Success message has not disappeared"
