import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# driver = webdriver.Firefox()

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL is:", get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Word is:", value_word)

    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = "screenshot" + now_date + ".png"
        self.driver.save_screenshot("S:\\pycharm\\projects\\SugaryFactory\\screen\\" + name_screenshot)
        print("Screenshot done")

    """Method assert URL"""

    def assert_URL(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good URL " + result)

    """Assert modal dialog"""



    def assert_modal_dialog_success_add(self, success):
        dialog_element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.dialog)))
        value_dialog = dialog_element.text
        assert success in value_dialog
        print("Modal dialog success")

    def assert_price_shopping_cart(self, price_field_1, price_field_2, total_field):
        value_price_1 = price_field_1.text.replace('$', '').replace(',', '')
        value_price_2 = price_field_2.text.replace('$', '').replace(',', '')
        value_total = total_field.text.replace('$', '').replace(',', '')
        summa = str(float(value_price_1) + float(value_price_2))
        summa = summa[0:6]
        print(value_price_1, value_price_2, value_total)
        assert summa == value_total
        print("Price shopping cart is:", value_price_1, value_price_2, "Total:", value_total)




