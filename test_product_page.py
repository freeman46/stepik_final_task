from .pages.product_page import ProductPage


def test_guest_can_add_product(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()

