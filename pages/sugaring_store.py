from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from base.base_class import Base
class SugarStore(Base):




    #Locators

    sugaring_store_all = "//a[text()='Sugaring Store']"

    select_product_1 = "(//div[@class='product-grid-item__image'])[1]"
    select_product_2 = "(//div[@class='product-grid-item__info'])[58]"
    button_add_to_cart = "//input[@id='button-cart']"
    main_word_page = "//h1[@class='category-header']"
    #options for the last item
    last_product_coffe = "(//div[@class='product-multiselect-option-box'])[4]"
    last_product_bamboo = "(//div[@class='product-multiselect-option-box'])[13]"
    last_product_charcoal = "(//div[@class='product-multiselect-option-box'])[20]"


    #model_dialog

    dialog = "//div[@id='notification']"



    #Getters

    def get_sugar_all(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sugaring_store_all)))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart)))

    def get_coffe(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.last_product_coffe)))
#options
    def get_bamboo(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.last_product_bamboo)))

    def get_charcoal(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.last_product_charcoal)))

    def get_main_word_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word_page)))




    #Actions

    def click_button_sugar_all(self):
        self.get_sugar_all().click()
        print("Button main store clicked")

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Selected product")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Selected product")

    def click_add_button_cart(self):
        self.get_button_cart().click()
        print("Button 'Add to cart' is clicked")

    # options for the last item

    def click_coffe(self):
        self.get_coffe().click()
        print("Option coffe is clicked")

    def click_bamboo(self):
        self.get_bamboo().click()
        print("Option bamboo is clicked")

    def click_charcoal(self):
        self.get_charcoal().click()
        print("Option charcoal is clicked")







    #Methods

    def select_item_1(self):
       self.click_button_sugar_all()
       self.assert_URL("https://test.sugaringfactory.com/sugaring-paste")
       self.assert_word(self.get_main_word_1(), "Sugaring Store")
       self.click_select_product_1()
       self.assert_URL("https://test.sugaringfactory.com/sugaring-paste/soft")
       self.click_add_button_cart()
       self.assert_modal_dialog_success_add("You have added") #checking modal_dialog


    def select_item_2(self):
       self.click_button_sugar_all()
       self.assert_URL("https://test.sugaringfactory.com/sugaring-paste")
       self.assert_word(self.get_main_word_1(), "Sugaring Store")
       self.driver.execute_script("window.scrollTo(0, 1000);")
       self.click_select_product_2()
       self.assert_URL("https://test.sugaringfactory.com/sugaring-paste/set-of-twelve-scrubs")
       self.click_coffe()
       self.click_bamboo()
       self.click_charcoal()
       self.click_add_button_cart()
       self.assert_modal_dialog_success_add("You have added") #checking modal_dialog




