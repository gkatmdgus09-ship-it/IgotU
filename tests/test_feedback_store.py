import tempfile
import unittest
from pathlib import Path

from feedback_store import add_suggestion, initialize_database, list_suggestions


class FeedbackStoreTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.database_path = Path(self.temp_dir.name) / "suggestions.db"
        initialize_database(self.database_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_rejects_empty_and_whitespace_only_suggestions(self):
        for content in ("", "   ", "\t\n"):
            with self.subTest(content=content):
                with self.assertRaises(ValueError):
                    add_suggestion(content, self.database_path)

    def test_suggestions_are_trimmed_and_listed_newest_first(self):
        add_suggestion("  먼저  ", self.database_path)
        add_suggestion("나중", self.database_path)

        self.assertEqual(list_suggestions(self.database_path), ["나중", "먼저"])


if __name__ == "__main__":
    unittest.main()
