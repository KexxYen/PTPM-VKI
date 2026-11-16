from pathlib import Path
import unittest
from unittest.mock import Mock, patch

from src.parser import ForumParser


FIXTURE = Path(__file__).parent / "fixtures" / "comments.html"
ARTICLE_URL = "https://habr.com/ru/companies/globalsign/articles/1102364/"


class ForumParserTests(unittest.TestCase):
    def make_response(self):
        response = Mock()
        response.text = FIXTURE.read_text(encoding="utf-8")
        return response

    @patch("src.parser.requests.get")
    def test_parse_first_comment(self, mock_get):
        mock_get.return_value = self.make_response()

        comments = ForumParser().parse_page(ARTICLE_URL)

        self.assertEqual(comments[0]["id"], 30591422)
        self.assertEqual(comments[0]["name"], "InsiderCrush")
        self.assertIn("Спасибо?", comments[0]["message"])
        mock_get.assert_called_once_with(
            ARTICLE_URL.rstrip("/") + "/comments/",
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10,
        )

    @patch("src.parser.requests.get")
    def test_parse_all_comments(self, mock_get):
        mock_get.return_value = self.make_response()

        comments = ForumParser().parse_page(ARTICLE_URL)

        self.assertEqual(len(comments), 9)
        for comment in comments:
            self.assertEqual( set(comment), {"id", "name", "message"})
            self.assertIsInstance(comment["id"], int)
            self.assertTrue(comment["name"])
            self.assertTrue(comment["message"])


if __name__ == "__main__":
    unittest.main()
