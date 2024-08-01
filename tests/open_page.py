from selenium import webdriver

from selenium.webdriver.firefox.service import Service

from pages.login_page import LoginPage


def test_open_page():
    service = Service('S:\\pycharm\\projects\\resource\\geckodriver.exe')
    driver = webdriver.Firefox(service=service)

    login = LoginPage(driver)
    login.authorization()

