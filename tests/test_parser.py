from pathlib import Path
import unittest
from unittest.mock import Mock
from src.parser import ForumParser

FIXTURE = Path("tests/fixtures/comments.html")

class ForumParserTests(unittest.TestCase):

    def test_parse_html(self):
        html = FIXTURE.read_text(encoding="utf-8")

        comments = ForumParser().parse_html(html)

        self.assertEqual(len(comments), 12)
        self.assertEqual(comments[0]["id"], 30643916)
        self.assertEqual(comments[0]["name"], "slackmanbozeman1110")
        self.assertIn("Думаю нет", comments[0]["message"])

    def test_save_to_db(self):
        repository = Mock()

        comments = [
            {
                "id": 1,
                "name": "User",
                "message": "Hello"
            }
        ]

        ForumParser().save_to_db(comments, repository)

        repository.add.assert_called_once_with(
            1, "User", "Hello"
        )


if __name__ == "__main__":
    unittest.main()
