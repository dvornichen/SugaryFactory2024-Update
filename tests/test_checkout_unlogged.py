from selenium import webdriver

from selenium.webdriver.firefox.service import Service

# from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.open_site import OpenPage
from pages.cart_page_unlog import CartPage

from pages.private_labeling import PrivateLabile
from pages.sugaring_store import SugarStore


def test_open_page():
    service = Service('S:\\pycharm\\projects\\resource\\geckodriver.exe')
    driver = webdriver.Firefox(service=service)

    open_website = OpenPage(driver)
    open_website.open_web()

    private_page = PrivateLabile(driver)
    private_page.private_buy()

    # login = LoginPage(driver)
    # login.authorization()
    #
    # ss_1 = SugarStore(driver)
    # ss_1.select_item_1()
    #
    # ss_2 = SugarStore(driver)
    # ss_2.select_item_2()
    #
    check = CartPage(driver)
    check.checkout()
