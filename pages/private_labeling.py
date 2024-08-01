import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from faker import Faker
faker = Faker("en_US")


driver = webdriver.Firefox()

from base.base_class import Base

class PrivateLabile(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    main_private_labeling = "//a[text()='Private Labeling']"
    category_sugar_paste = "//div[text()='Sugar Paste']" #choose the category
    product_tubes = "//div[text()='Tubes']" #choose the product
    choose_size = "//div[text()='35 oz clear']" #choose size
    #quantity
    soft_quantity = "(//input)[2]"
    gentle_quantity = "(//input)[3]"
    ultra_quantity = "(//input)[4]"
    ultima_quantity = "(//input)[5]"
    save_proceed_button_1 = "(//button[text()='Save & Proceed'])[1]"
    #setup labeling
    choose_design = "//div[text()='Choose my design']"
    ready_design = "//div[text()='Ready to label']"
    #upload photo
    #path_upload = "S:\\pycharm\\projects\\SugaryFactory\\photo_test\\merc.jpg"
    button_send = "//div[@class='pl__upload']"
    save_proceed_button_2 = "(//button[text()='Save & Proceed'])[2]"
    #sign agreement
    read_and_sign_button = "//span[text()='Read and Sign']"
    #agreement
    iframe = "//iframe[@class='accept-license-agreement-iframe']"
    main_words_assert = "//strong[contains(text(), 'PRIVATE LABEL SELECTOR')]"
    agree_and_sign_button = "//button[contains(text(), 'Agree and Sign')]"
    first_name_field = "//input[@name='firstName']"
    last_name_field = "//input[@name='lastName']"
    email_field = "//input[@name='email']"
    date_of_birth_field = "//input[@name='birthdate']" # # new_data.send_keys('10/10/2025')
    state_field = "//input[@name='region']"
    city_field = "//input[@name='city']"
    zip_field = "//input[@name='zip']"
    street_field = "//input[@name='street1']"
    sign_and_submit_button = "//button[@type='submit']"

    #Getters

    def get_main_private_labeling_page(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_private_labeling)))

    def get_category_sugar_paste(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.category_sugar_paste)))

    def get_product_tubes(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_tubes)))

    def get_choose_size(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.choose_size)))

   #quantity

    def get_soft_quantity(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.soft_quantity)))

    def get_gentle_quantity(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.gentle_quantity)))

    def get_ultra_quantity(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.ultra_quantity)))

    def get_ultima_quantity(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.ultima_quantity)))
    #design

    def get_choose_design(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.choose_design)))

    def get_ready_design(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.ready_design)))

    #send photo

    def get_button_send(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_send)))

    def get_save_proceed_button_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.save_proceed_button_2)))

    def get_save_proceed_button_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.save_proceed_button_1)))

    #sign

    def get_read_and_sign_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.read_and_sign_button)))

    def get_iframe(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.iframe)))

    def get_main_words_assert(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_words_assert)))

    def get_agree_and_sign_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.agree_and_sign_button)))

    def get_first_name_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_name_field)))

    def get_last_name_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.last_name_field)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_date_of_birth_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.date_of_birth_field)))

    def get_state_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.state_field)))

    def get_city_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.city_field)))

    def get_zip_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.zip_field)))

    def get_street_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.street_field)))

    def get_sign_and_submit_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sign_and_submit_button)))


    #Actions

    def click_main_private_labeling_page(self):
        self.get_main_private_labeling_page().click()
        print("Private Labeling Page Clicked")

    def click_category_sugar_paste(self):
        self.get_category_sugar_paste().click()
        print("Sugar Paste Clicked")

    def click_product_tubes(self):
        self.get_product_tubes().click()
        print("Tubes is clicked")

    def click_choose_size(self):
        self.get_choose_size().click()
        print("Size Clicked")

    #quantity

    def input_soft_quantity(self, soft_quantity):
        self.get_soft_quantity().send_keys(soft_quantity)
        print("Soft Quantity Entered")

    def input_gentle_quantity(self, gentle_quantity):
        self.get_gentle_quantity().send_keys(gentle_quantity)
        print("Gentle Quantity Entered")

    def input_ultra_quantity(self, ultra_quantity):
        self.get_ultra_quantity().send_keys(ultra_quantity)
        print("Ultra Quantity Entered")

    def input_ultima_quantity(self, ultima_quantity):
        self.get_ultima_quantity().send_keys(ultima_quantity)
        print("Ultima Quantity Entered")

    def click_save_proceed_button_2(self):
        self.get_save_proceed_button_2().click()
        print("Save and proceed Clicked")

    def click_save_proceed_button_1(self):
        self.get_save_proceed_button_1().click()
        print("Save and proceed Clicked")

    #design

    def click_choose_design(self):
        self.get_choose_design().click()
        print("Design Clicked")

    def click_ready_design(self):
        self.get_ready_design().click()
        print("Ready Design Clicked")

    def send_photo(self, path):
        self.get_button_send().send_keys(path)
        print("Photo Send")

    #terms

    def click_read_and_sign_button(self):
        self.get_read_and_sign_button().click()
        print("Read and Sign Clicked")

    def click_agree_and_sign_button(self):
        actions = ActionChains(self.driver)
        button = self.get_agree_and_sign_button()
        actions.move_to_element(button).click().perform()
        print("Agree and Sign Clicked with ActionChains")

    def input_first_name(self, first_name_field):
        self.get_first_name_field().send_keys(first_name_field)
        print("Input First Name")

    def input_last_name(self, last_name_field):
        self.get_last_name_field().send_keys(last_name_field)
        print("Input Last Name")


    def input_email(self, email_field):
        self.get_email_field().send_keys(email_field)
        print("Input email")

    def input_date_of_birth(self, date_of_birth_field):
        self.get_date_of_birth_field().send_keys(date_of_birth_field)
        print("Input Date of Birth")

    def input_state(self, state_field):
        self.get_state_field().send_keys(state_field)
        print("Input state")

    def input_city(self, city_field):
        self.get_city_field().send_keys(city_field)
        print("Input city")

    def input_zip(self, zip_field):
        self.get_zip_field().send_keys(zip_field)
        print("Input Zipcode")

    def input_street(self, street_field):
        self.get_street_field().send_keys(street_field)
        print("Input name of street")

    def click_sign_and_submit_button(self):
        actions = ActionChains(self.driver)
        button = self.get_sign_and_submit_button()
        actions.move_to_element(button).click().perform()
        print("Sign And Submit Clicked with ActionChains")




    #Methods

    def private_buy(self):
        self.click_main_private_labeling_page()
        self.get_current_url()
        self.assert_URL("https://test.sugaringfactory.com/private-labeling")
        self.click_category_sugar_paste()
        self.click_product_tubes()
        self.click_choose_size()

        self.input_soft_quantity(23)
        self.input_gentle_quantity(25)
        self.input_ultra_quantity(100)
        self.input_ultima_quantity(111)

        self.click_save_proceed_button_1()
        # self.click_choose_design()
        self.click_ready_design()


        self.click_read_and_sign_button()


        iframe_element = self.get_iframe()
        self.driver.switch_to.frame(iframe_element)        #Switch to iframe before clicking the button

        self.assert_word(self.get_main_words_assert(), "PRIVATE LABEL SELECTOR AND MANUFACTURING AGREEMENT")
        self.click_agree_and_sign_button()

        self.input_first_name("tester." + faker.first_name())
        self.input_last_name("tester." + faker.last_name())
        self.input_email("tester@tester.gmail.com")
        self.input_state("New-Jersey")
        self.input_zip("tester." + faker.zipcode())
        self.input_city("tester." + faker.city())
        self.input_street("tester.street 30")
        self.input_date_of_birth("1999-02-01")

        self.click_sign_and_submit_button()
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
