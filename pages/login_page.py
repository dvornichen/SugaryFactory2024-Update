import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base

class LoginPage(Base):

    url = 'https://test.sugaringfactory.com/'



    #Locators

    button_add_cart = "(//a[@class='menu-item _login'])[2]"
    email = "//input[@name='email']"
    password = "//input[@name='password']"
    login_button = "(//a[@class='button-cont-right'])[2]"
    main_word_1 = "//h1[text()='Account Login']"
    main_word_2 = "//h2[text()='My Account']"



    #Getters

    def get_login_page(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_add_cart)))

    def get_email(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word_1)))

    def get_main_word_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word_2)))

    #Actions

    def click_login_page(self):
        self.get_login_page().click()
        print("Login page is clicked")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input Email")


    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input Password")

    def click_login(self):
        self.get_login_button().click()
        print("Login button entered")



    #Methods

    def authorization(self):
        self.driver.get(self.url)
        self.get_current_url()
        self.click_login_page()
        self.get_current_url()
        self.assert_word(self.get_main_word_1(), "Account Login")
        self.assert_URL("https://test.sugaringfactory.com/index.php?route=account%2Flogin")
        self.input_email("tester@tester.gmail.com")
        self.input_password('testeralex')
        self.click_login()
        self.assert_word(self.get_main_word_2(), "My Account")
        self.assert_URL("https://test.sugaringfactory.com/index.php?route=account%2Faccount")