
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from datetime import datetime
import time 

class CalculatorPage:

    URL = "https://www.globalsqa.com/angularJs-protractor/SimpleCalculator/"

    def __init__(self, driver):
        self.driver = driver

        self._first_number = (By.XPATH, "(//input)[1]")
        self._second_number = (By.XPATH, "(//input)[2]")
        self._operation = (By.TAG_NAME, "select")

    def open(self):
        self.driver.get(self.URL)

    def enter_first_number(self, number):
        element = self.driver.find_element(*self._first_number)
        element.clear()
        element.send_keys(str(number))
        time.sleep(0.5)

    def enter_second_number(self, number):
        element = self.driver.find_element(*self._second_number)
        element.clear()
        element.send_keys(str(number))
        time.sleep(0.5)

    def select_operation(self, operation):
        element = self.driver.find_element(*self._operation)
        Select(element).select_by_visible_text(operation)
        time.sleep(0.5)

    def calculate(self):
        pass
    
    def get_result(self):
        text = self.driver.find_element(By.TAG_NAME, "body").text
        time.sleep(0.5)
        return text.split("=")[-1].strip()

