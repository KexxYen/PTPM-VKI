import unittest
import datetime

from Delivery import calculate_delivery_cost


class DeliveryTests(unittest.TestCase):
    def test_regular_delivery(self):
        expected_date = datetime.date.today() + datetime.timedelta(days=1)
        self.assertEqual(calculate_delivery_cost(1, 100, "обычный"), (700, expected_date.isoformat()))

    def test_minimum_weight(self):
        self.assertEqual(calculate_delivery_cost(0.1, 100, "обычный")[0], 700)

    def test_weight_below_minimum(self):
        self.assertEqual(calculate_delivery_cost(0.09, 100, "обычный"), (-1, "0000-00-00"))

    def test_maximum_weight(self):
        self.assertEqual(calculate_delivery_cost(50, 100, "обычный")[0], 1050)

    def test_weight_above_maximum(self):
        self.assertEqual(calculate_delivery_cost(50.01, 100, "обычный"), (-1, "0000-00-00"))

    def test_minimum_distance(self):
        expected_date = datetime.date.today() + datetime.timedelta(days=1)
        self.assertEqual(calculate_delivery_cost(1, 1, "обычный"), (205, expected_date.isoformat()))

    def test_distance_below_minimum(self):
        self.assertEqual(calculate_delivery_cost(1, 0, "обычный"), (-1, "0000-00-00"))

    def test_maximum_distance(self):
        expected_date = datetime.date.today() + datetime.timedelta(days=10)
        self.assertEqual(calculate_delivery_cost(1, 5000, "обычный"), (25200, expected_date.isoformat()))

    def test_distance_above_maximum(self):
        self.assertEqual(calculate_delivery_cost(1, 5001, "обычный"), (-1, "0000-00-00"))

    def test_unknown_package_type(self):
        self.assertEqual(calculate_delivery_cost(1, 100, "неизвестный"), (-1, "0000-00-00"))

    def test_empty_package_type(self):
        self.assertEqual(calculate_delivery_cost(1, 100, ""), (-1, "0000-00-00"))

    def test_weight_exactly_five(self):
        self.assertEqual(calculate_delivery_cost(5, 100, "обычный")[0], 700)

    def test_weight_above_five(self):
        self.assertEqual(calculate_delivery_cost(5.01, 100, "обычный")[0], 840)

    def test_weight_below_twenty(self):
        self.assertEqual(calculate_delivery_cost(19.99, 100, "обычный")[0], 840)

    def test_weight_exactly_twenty(self):
        self.assertEqual(calculate_delivery_cost(20, 100, "обычный")[0], 1050)

    def test_fragile_package(self):
        self.assertEqual(calculate_delivery_cost(1, 100, "хрупкий")[0], 1000)

    def test_dangerous_package(self):
        self.assertEqual(calculate_delivery_cost(1, 100, "опасный")[0], 1700)

    def test_weight_coefficient_before_surcharge(self):
        self.assertEqual(calculate_delivery_cost(20, 100, "хрупкий")[0], 1350)

    def test_distance_exactly_five_hundred(self):
        expected_date = datetime.date.today() + datetime.timedelta(days=1)
        self.assertEqual(calculate_delivery_cost(1, 500, "обычный")[1], expected_date.isoformat())

    def test_distance_just_above_five_hundred(self):
        expected_date = datetime.date.today() + datetime.timedelta(days=2)
        self.assertEqual(calculate_delivery_cost(1, 501, "обычный")[1], expected_date.isoformat())

    def test_partial_third_day(self):
        expected_date = datetime.date.today() + datetime.timedelta(days=3)
        self.assertEqual(calculate_delivery_cost(1, 1499, "обычный")[1], expected_date.isoformat())

    def test_express_costs_more(self):
        regular = calculate_delivery_cost(1, 100, "обычный")[0]
        express = calculate_delivery_cost(1, 100, "обычный", True)[0]
        self.assertGreater(express, regular)

    def test_express_takes_at_least_one_day(self):
        expected_date = datetime.date.today() + datetime.timedelta(days=1)
        self.assertEqual(calculate_delivery_cost(1, 100, "обычный", True)[1], expected_date.isoformat())

    def test_express_rounds_partial_day_up(self):
        expected_date = datetime.date.today() + datetime.timedelta(days=2)
        self.assertEqual(calculate_delivery_cost(1, 1500, "обычный", True)[1], expected_date.isoformat())

    def test_express_even_number_of_days(self):
        expected_date = datetime.date.today() + datetime.timedelta(days=2)
        self.assertEqual(calculate_delivery_cost(1, 2000, "обычный", True)[1], expected_date.isoformat())




if __name__ == "__main__":
    unittest.main()
