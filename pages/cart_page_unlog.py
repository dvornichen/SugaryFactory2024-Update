import time
from selenium.webdriver.support.ui import Select

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Firefox()

from base.base_class import Base

class CartPage(Base):

    # Locators for various elements on the cart page
    cart_button = "//div[@id ='cart']"
    button_checkout = "//span[text()='Checkout']"
    button_continue_checkout = "(//a[@class='button-prod'])[2]" #shopping cart page
    #shopping_data fields
    first_name = "//input[@name='firstname']"
    last_name = "//input[@name='lastname']"
    email = "//input[@name='email']"
    phone = "//input[@name='telephone']"
    state = "//select[@id='zone_id']" #dropdown for state selection
    city = "//input[@name='city']"
    address = "//input[@name='address_1']"
    zip = "//input[@name='postcode']"

    #payment data fields

    payment_data_checkbox = "(//input[@name='payment_address_same_as_shipping'])[2]"

    checkbox_signature = "//input[@name='signature_is_required']"
    comment_field = "//textarea[@name='comment']"
    checkbox_cash = "//input[@id='cod']"
    checkbox_delivery_terms = "//input[@class='accept-checkbox']"
    accept_button = "(//a[@class='button'])[2]" # button to accept terms
    confirm_button = "//button[@id='checkout-submit-button']" #first confirmation button
    confirm_button_2 = "//a[@id='button-confirm']" #second confirmation button
    #checking price
    price_field_1 = "(//td[@class='total'])[1]"
    price_field_2 = "(//td[@class='total'])[2]"
    total_field = "//td[@class='right cart-total1 last']"

    #$213.47

    #words for asserts

    shopping_cart_word = "//a[@class='last']"
    checkout_word = "//h1[text()='Checkout']"

    # Getters
    def get_cart_icon(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_checkout)))
    def get_button_continue_checkout(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_continue_checkout)))

    def get_checkbox_signature(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_signature)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_email(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_telephone(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_state(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.state)))

    def get_city(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_address(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_zip(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.zip)))

    def  get_payment_data_checkbox(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.payment_data_checkbox)))

    def get_comment_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.comment_field)))

    def get_checkbox_cash(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_cash)))

    def get_checkbox_delivery_terms(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_delivery_terms)))

    def get_accept_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.accept_button )))

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.confirm_button)))

    def get_confirm_button_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.confirm_button_2)))

    def get_shopping_cart_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.shopping_cart_word)))

    def get_checkout_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkout_word)))

    def get_price_field_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_field_1)))

    def get_price_field_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_field_2)))

    def get_total_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.total_field)))



    # Actions
    def hover_over_cart_icon(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_cart_icon()).perform()
        self.driver.implicitly_wait(10)
        time.sleep(2)
        print("Hovered the mouse over the icon 'Cart'")

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Checkout button clicked")

    def click_button_continue_checkout(self):
        self.get_button_continue_checkout().click()
        print("Continue checkout button clicked")

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("First Name input")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Last Name input")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Email input")

    def input_telephone(self, phone):
        self.get_telephone().send_keys(phone)
        print("Telephone input")

    def select_state(self):
        select_element = self.get_state()
        select = Select(select_element)
        select.select_by_value("3653")
        print("State selected")

    def input_city(self, city):
        self.get_city().send_keys(city)
        print("City input")

    def input_address(self, address):
        self.get_address().send_keys(address)
        print("Address input")

    def input_zip(self, zip):
        self.get_zip().send_keys(zip)
        print("Zip input")

    def click_payment_data_checkbox(self):
        self.get_payment_data_checkbox().click()
        print("Checkbox payment clicked")
    def click_checkbox_signature(self):
        self.get_checkbox_signature().click()
        print("Checkbox signature clicked")

    def input_comment_field(self, comment_field):
        self.get_comment_field().send_keys(comment_field)
        print("Comment field is full")

    def click_checkbox_cash(self):
        self.get_checkbox_cash().click()
        print("checkbox cash clicked")

    def click_checkbox_delivery_terms(self):
        self.get_checkbox_delivery_terms().click()
        print("checkbox delivery terms clicked")

    def click_accept_button(self):
        self.get_accept_button().click()
        print("accept button clicked")

    def click_confirm_button(self):
        self.get_confirm_button().click()
        print("confirm button clicked")

    def click_confirm_button_2(self):
        self.get_confirm_button_2().click()
        print("confirm 2 button clicked")




    # Methods
    def checkout(self):
        self.hover_over_cart_icon()
        self.click_checkout_button()
        self.assert_URL("https://test.sugaringfactory.com/index.php?route=checkout%2Fcart")
        self.assert_word(self.get_shopping_cart_word(), "Shopping Cart")

        self.click_button_continue_checkout()
        self.assert_word(self.get_checkout_word(), "Checkout")
        self.input_first_name("test.Antonio")
        self.input_last_name("test.Banderas")
        self.input_email("tester@tester.gmail.com")
        self.input_telephone("555-555-5555")
        self.input_city("Bangalore")
        self.input_address("Tester Address 30")
        self.input_zip("12345")
        self.select_state()
        self.click_payment_data_checkbox()
        self.driver.execute_script("window.scrollTo(0, 400);")
        self.click_checkbox_signature()
        self.input_comment_field(" TEST ALEX IT'S FOR YOU! ")
        self.click_checkbox_cash()
        self.driver.execute_script("window.scrollTo(0, 200);")
        self.click_checkbox_delivery_terms()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 200);")
        self.click_accept_button()
        time.sleep(3)
        self.click_confirm_button()
        self.click_confirm_button_2()
        self.get_screenshot()
        print("Checkout process completed!")