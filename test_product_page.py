import pytest

from .pages.product_page import ProductPage

promo_list = [
    '?promo=newYear',
    '?promo=newYear2019',
    '?promo=offer0',
    '?promo=offer1',
    '?promo=offer2',
    '?promo=offer3',
    '?promo=offer4',
    '?promo=offer5',
    '?promo=offer6',
    pytest.param('?promo=offer7', marks=pytest.mark.xfail(reason='broken test')),
    '?promo=offer8',
    '?promo=offer9'
]


@pytest.mark.parametrize('promo', promo_list)
def test_guest_can_add_product(browser, promo):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()


@pytest.mark.xfail(reason='broken test')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_in_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason='broken test')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_in_basket()
    product_page.should_not_be_present_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()