
import unittest
from selenium import webdriver
from pages.calculator_page import CalculatorPage
import os
from datetime import datetime

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = CalculatorPage(self.driver)
        self.page.open()

    def tearDown(self):
        os.makedirs("screenshots", exist_ok=True)
        test_name = self._testMethodName
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        screenshot_path = f"screenshots/{test_name}_{timestamp}.png"

        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    # Сложение
    def test_addition(self):
        self.page.enter_first_number(10)
        self.page.enter_second_number(5)
        self.page.select_operation("+")
        self.page.calculate()
        self.assertEqual(self.page.get_result(), "15")

    # Вычитание
    def test_subtraction(self):
        self.page.enter_first_number(10)
        self.page.enter_second_number(5)
        self.page.select_operation("-")
        self.page.calculate()

        self.assertEqual(self.page.get_result(), "5")

    # Умножение
    def test_multiplication(self):
        self.page.enter_first_number(10)
        self.page.enter_second_number(5)
        self.page.select_operation("*")
        self.page.calculate()

        self.assertEqual(self.page.get_result(), "50")

    # Деление
    def test_division(self):
        self.page.enter_first_number(10)
        self.page.enter_second_number(2)
        self.page.select_operation("/")
        self.page.calculate()

        self.assertEqual(self.page.get_result(), "5")

    # Проверка отрицательного результата
    def test_negative_result(self):
        self.page.enter_first_number(5)
        self.page.enter_second_number(10)
        self.page.select_operation("-")
        self.page.calculate()

        self.assertEqual(self.page.get_result(), "-5")

    # Проверка умножения на ноль
    def test_multiplication_by_zero(self):
        self.page.enter_first_number(10)
        self.page.enter_second_number(0)
        self.page.select_operation("*")
        self.page.calculate()

        self.assertEqual(self.page.get_result(), "0")

    # Проверка деления на ноль
    def test_subtraction_by_zero(self):
        self.page.enter_first_number(10)
        self.page.enter_second_number(0)
        self.page.select_operation("/")
        self.page.calculate()
        
        self.assertEqual(self.page.get_result(), "null")

if __name__ == "__main__":
    unittest.main()
