import unittest

from main import calc_triangle


class TriangleTests(unittest.TestCase):
    # Функция возвращает тип треугольника и координаты.
    # assertEqual сравнивает полученный результат с ожидаемым.
    def test_equilateral_triangle(self):
        triangle_type, coordinates = calc_triangle('4', '4', '4')
        self.assertEqual(triangle_type, 'равносторонний')

    def test_isosceles_first_two_sides(self):
        triangle_type, coordinates = calc_triangle('5', '5', '6')
        self.assertEqual(triangle_type, 'равнобедренный')

    def test_isosceles_first_and_last_sides(self):
        triangle_type, coordinates = calc_triangle('5', '6', '5')
        self.assertEqual(triangle_type, 'равнобедренный')

    def test_isosceles_last_two_sides(self):
        triangle_type, coordinates = calc_triangle('6', '5', '5')
        self.assertEqual(triangle_type, 'равнобедренный')

    def test_scalene_triangle(self):
        triangle_type, coordinates = calc_triangle('3', '4', '5')
        self.assertEqual(triangle_type, 'разносторонний')

    def test_decimal_sides(self):
        triangle_type, coordinates = calc_triangle('1.5', '2', '2.5')
        self.assertEqual(triangle_type, 'разносторонний')

    def test_spaces_around_numbers(self):
        triangle_type, coordinates = calc_triangle(' 3 ', ' 4 ', ' 5 ')
        self.assertEqual(triangle_type, 'разносторонний')

    def test_text_in_first_side(self):
        triangle_type, coordinates = calc_triangle('abc', '4', '5')
        self.assertEqual(triangle_type, '')

    def test_text_in_second_side(self):
        triangle_type, coordinates = calc_triangle('3', 'abc', '5')
        self.assertEqual(triangle_type, '')

    def test_text_in_third_side(self):
        triangle_type, coordinates = calc_triangle('3', '4', 'abc')
        self.assertEqual(triangle_type, '')

    def test_empty_string(self):
        triangle_type, coordinates = calc_triangle('', '4', '5')
        self.assertEqual(triangle_type, '')

    def test_comma_in_number(self):
        triangle_type, coordinates = calc_triangle('3,5', '4', '5')
        self.assertEqual(triangle_type, '')

    def test_zero_first_side(self):
        triangle_type, coordinates = calc_triangle('0', '4', '5')
        self.assertEqual(triangle_type, 'не треугольник')

    def test_zero_second_side(self):
        triangle_type, coordinates = calc_triangle('3', '0', '5')
        self.assertEqual(triangle_type, 'не треугольник')

    def test_zero_third_side(self):
        triangle_type, coordinates = calc_triangle('3', '4', '0')
        self.assertEqual(triangle_type, 'не треугольник')

    def test_negative_side(self):
        triangle_type, coordinates = calc_triangle('-3', '4', '5')
        self.assertEqual(triangle_type, 'не треугольник')

    def test_sum_less_than_longest(self):
        triangle_type, coordinates = calc_triangle('1', '2', '4')
        self.assertEqual(triangle_type, 'не треугольник')

    def test_sum_equals_longest(self):
        triangle_type, coordinates = calc_triangle('1', '4', '5')
        self.assertEqual(triangle_type, 'не треугольник')

    def test_coordinates_for_triangle(self):
        triangle_type, coordinates = calc_triangle("3", "4", "5")
        self.assertEqual(coordinates, [(10, 10), (90, 10), (61, 48)])

    def test_coordinates_for_invalid_numbers(self):
        triangle_type, coordinates = calc_triangle("0", "4", "5")
        self.assertEqual(coordinates, [(-1, -1), (-1, -1), (-1, -1)])

    def test_coordinates_for_text(self):
        triangle_type, coordinates = calc_triangle("abc", "4", "5")
        self.assertEqual(coordinates, [(-2, -2), (-2, -2), (-2, -2)])


if __name__ == "__main__":
    unittest.main()
