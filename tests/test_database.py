import sqlite3
import unittest

from src.database import DatabaseRepository


class DatabaseRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.repository = DatabaseRepository(":memory:")

    def tearDown(self):
        self.repository.close()

    def test_add_success(self):
        result = self.repository.add(1, "user1", "Первый комментарий")

        self.assertTrue(result)
        self.assertEqual(
            self.repository.get_by_id(1),
            {"id": 1, "name": "user1", "message": "Первый комментарий"},
        )

    def test_add_duplicate_id_raises_error(self):
        self.repository.add(1, "user1", "Первый комментарий")

        with self.assertRaises(sqlite3.IntegrityError):
            self.repository.add(1, "user2", "Другой комментарий")

    def test_add_rejects_long_username(self):
        with self.assertRaises(ValueError):
            self.repository.add(1, "u" * 257, "Комментарий")

    def test_add_rejects_long_message(self):
        with self.assertRaises(ValueError):
            self.repository.add(1, "user1", "т" * 8097)

    def test_add_rejects_non_integer_id(self):
        with self.assertRaises(TypeError):
            self.repository.add("1", "user1", "Комментарий")

    def test_get_by_id_returns_record(self):
        self.repository.add(1, "user1", "Комментарий")

        result = self.repository.get_by_id(1)

        self.assertEqual(result["name"], "user1")

    def test_get_by_id_returns_none_when_missing(self):
        self.assertIsNone(self.repository.get_by_id(99))

    def test_get_by_name_returns_all_users_records(self):
        self.repository.add(1, "user1", "Первый")
        self.repository.add(2, "user1", "Второй")
        self.repository.add(3, "user2", "Чужой")

        result = self.repository.get_by_name("user1")

        self.assertEqual([comment["id"] for comment in result], [1, 2])

    def test_get_by_name_returns_empty_list_when_missing(self):
        self.assertEqual(self.repository.get_by_name("unknown"), [])

    def test_update_changes_message(self):
        self.repository.add(1, "user1", "Старый текст")

        result = self.repository.update(1, "Новый текст")

        self.assertTrue(result)
        self.assertEqual(self.repository.get_by_id(1)["message"], "Новый текст")

    def test_update_returns_false_when_id_missing(self):
        self.assertFalse(self.repository.update(99, "Новый текст"))

    def test_update_rejects_long_message(self):
        self.repository.add(1, "user1", "Старый текст")

        with self.assertRaises(ValueError):
            self.repository.update(1, "т" * 8097)

    def test_delete_removes_record(self):
        self.repository.add(1, "user1", "Комментарий")

        result = self.repository.delete(1)

        self.assertTrue(result)
        self.assertIsNone(self.repository.get_by_id(1))

    def test_delete_returns_false_when_id_missing(self):
        self.assertFalse(self.repository.delete(99))


if __name__ == "__main__":
    unittest.main()
