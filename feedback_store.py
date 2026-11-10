from contextlib import closing
import sqlite3


def initialize_database(database_path):
    with closing(sqlite3.connect(database_path)) as connection:
        with connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS suggestions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL
                )
                """
            )


def add_suggestion(content, database_path):
    normalized_content = content.strip()
    if not normalized_content:
        raise ValueError("Suggestion content cannot be empty.")

    with closing(sqlite3.connect(database_path)) as connection:
        with connection:
            connection.execute(
                "INSERT INTO suggestions (content) VALUES (?)",
                (normalized_content,),
            )


def list_suggestions(database_path):
    with closing(sqlite3.connect(database_path)) as connection:
        rows = connection.execute(
            "SELECT content FROM suggestions ORDER BY id DESC"
        ).fetchall()
    return [row[0] for row in rows]
