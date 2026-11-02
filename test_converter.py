import unittest

from converter import Converter


class TestConverter(unittest.TestCase):
    def test_positive_values_and_upper_boundary(self):
        self.assertEqual(Converter.do(0.1), 0)
        self.assertEqual(Converter.do(65.7), 65)
        self.assertEqual(Converter.do(100.6), 100)
        self.assertEqual(Converter.do(100.7), 1000)
        self.assertEqual(Converter.do(150.0), 1000)

    def test_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            Converter.do(0.0)

    def test_negative_values_and_boundary(self):
        self.assertEqual(Converter.do(-0.1), -5)
        self.assertEqual(Converter.do(-30.4), -35)

    def test_values_below_negative_boundary(self):
        self.assertEqual(Converter.do(-30.5), -2000)
        self.assertEqual(Converter.do(-94.5), -2000)


if __name__ == "__main__":
    unittest.main()
    