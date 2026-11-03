import unittest

from converter import Converter


class TestConverter(unittest.TestCase):

    def test_positive_number(self):
        self.assertEqual(Converter.do(65.7), 65)

    def test_positive_upper_boundary(self):
        self.assertEqual(Converter.do(100.7), 1000)

    def test_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            Converter.do(0.0)

    def test_negative_number(self):
        self.assertEqual(Converter.do(-15.8), -20)

    def test_number_just_above_lower_boundary(self):
        self.assertEqual(Converter.do(-30.4), -35)

    def test_number_below_lower_boundary(self):
        self.assertEqual(Converter.do(-30.5), -2000)

    def test_number_just_below_upper_boundary(self):
        self.assertEqual(Converter.do(100.6), 100)

    def test_number_just_above_lower_boundary(self):
        self.assertEqual(Converter.do(-30.3), -35)

    def test_large_negative_number(self):
        self.assertEqual(Converter.do(-94.5), -2000)


if __name__ == "__main__":
    unittest.main()


