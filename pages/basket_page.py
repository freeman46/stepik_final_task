from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_do_not_exist_product(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "The basket contains products, but shouldn't."

    def should_be_present_message_of_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_OF_EMPTY_BASKET), \
            "Message of empty basket do not exist!"
