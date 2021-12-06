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
    '?promo=offer7',
    '?promo=offer8',
    '?promo=offer9'
]


@pytest.mark.parametrize('promo', promo_list)
def test_guest_can_add_product(browser, promo):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
