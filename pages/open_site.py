import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base

class OpenPage(Base):

    url = 'https://test.sugaringfactory.com/'
    def open_web(self):
        self.driver.get(self.url)
        self.get_current_url()