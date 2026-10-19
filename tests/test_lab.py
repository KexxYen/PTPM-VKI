import unittest
from unittest.mock import Mock, patch

from Controller import Controller
from Database import Database
from ExternalService import ExternalService
from TriangleCalculate import TriangleCalculate
from UserInteraction import ConsoleUserInteraction, UserInteraction


class LabTests(unittest.TestCase):
    def setUp(self):
        self.database = Database(":memory:")
        self.user = Mock(spec=UserInteraction)
        self.user.get_data.return_value = (3, 4, 5)
        self.service = Mock(spec=ExternalService)
        self.calculator = TriangleCalculate()
        self.controller = Controller(
            self.user, self.calculator, self.database, self.service
        )

    def tearDown(self):
        self.database.close()

    # Интеграционный тест: расчёт + сохранение + отправка.
    def test_new_result(self):
        result = self.controller.run()

        self.assertEqual(result, "Тип треугольника: разносторонний")
        self.assertEqual(
            self.database.get_triangle(3, 4, 5),
            ("разносторонний", None)
        )
        self.service.send.assert_called_once_with(result)

    # Интеграционный тест: получить и отправить уже сохранённый результат.
    def test_saved_result(self):
        self.database.add_triangle(3, 4, 5, "разносторонний")

        result = self.controller.run()

        self.assertEqual(result, "Тип треугольника: разносторонний")
        self.service.send.assert_called_once_with(result)

    # Интеграционный тест: сохранение и отправка ошибки расчёта.
    def test_invalid_triangle(self):
        self.user.get_data.return_value = (5, 5, 10)

        result = self.controller.run()

        error = "Ошибка: сумма двух сторон должна быть больше третьей"
        data = self.database.get_triangle(5, 5, 10)

        self.assertEqual(data, ("не треугольник", error))
        self.assertEqual(result, "Тип треугольника: не треугольник. " + error)
        self.service.send.assert_called_once_with(result)

    # Проверка консольного ввода без ручного ввода в тесте.
    def test_user_input(self):
        with patch("builtins.input", side_effect=["3.5", "4", "5"]):
            sides = ConsoleUserInteraction().get_data()

        self.assertEqual(sides, (3.5, 4.0, 5.0))

    # Проверка удаления записи из БД.
    def test_delete_triangle(self):
        self.database.add_triangle(3, 4, 5, "разносторонний")

        deleted = self.database.delete_triangle(3, 4, 5)

        self.assertEqual(deleted, 1)
        self.assertIsNone(self.database.get_triangle(3, 4, 5))
