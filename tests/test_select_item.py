from selenium import webdriver

from selenium.webdriver.firefox.service import Service

from pages.login_page import LoginPage
from pages.sugaring_store import SugarStore


def test_open_page():
    service = Service('S:\\pycharm\\projects\\resource\\geckodriver.exe')
    driver = webdriver.Firefox(service=service)

    login = LoginPage(driver)
    login.authorization()

    select_1 = SugarStore(driver)
    select_1.select_item_1()

    select_2 = SugarStore(driver)
    select_2.select_item_2()