import unittest
from PyQt5.QtWidgets import QApplication, QPushButton
from calculator import Calculator

app = QApplication([])

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def click_button(self, button_text):
        button = self.find_button(button_text)
        if button is not None:
            button.click()
        else:
            raise ValueError(f'Button with text "{button_text}" not found')

    def find_button(self, button_text):
        for button in self.calc.findChildren(QPushButton):
            if button.text() == button_text:
                return button
        return None

    def test_addition(self):
        self.calc.result.setText("2+3")
        self.click_button('=')
        self.assertEqual(self.calc.result.text(), "5")

    def test_subtraction(self):
        self.calc.result.setText("5-3")
        self.click_button('=')
        self.assertEqual(self.calc.result.text(), "2")

    def test_multiplication(self):
        self.calc.result.setText("3*3")
        self.click_button('=')
        self.assertEqual(self.calc.result.text(), "9")

    def test_division(self):
        self.calc.result.setText("9/3")
        self.click_button('=')
        self.assertEqual(self.calc.result.text(), "3.0")

    def test_clear(self):
        self.calc.result.setText("9/3")
        self.click_button('C')
        self.assertEqual(self.calc.result.text(), "")

    def test_clear_entry(self):
        self.calc.result.setText("9/3")
        self.click_button('CE')
        self.assertEqual(self.calc.result.text(), "9/")

    def test_float_comparison(self):
        self.calc.result.setText("9/2")
        self.click_button('=')
        self.assertAlmostEqual(float(self.calc.result.text()), 4.5)

    # testing for button clicks and button text
    def test_button_clicks(self):
        self.click_button('1')
        self.assertEqual(self.calc.result.text(), "1")
        self.click_button('+')
        self.assertEqual(self.calc.result.text(), "1+")



if __name__ == '__main__':
    unittest.main()
