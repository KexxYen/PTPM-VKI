import sqlite3


class DatabaseRepository:
    """Простой репозиторий комментариев на SQLite."""

    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL CHECK(length(name) <= 256),
                message TEXT NOT NULL CHECK(length(message) <= 8096)
            )
            """
        )
        self.connection.commit()

    def validate_text(self, value, field, max_length):
        if not isinstance(value, str):
            raise TypeError(f"{field} должен быть строкой")
        if not value:
            raise ValueError(f"{field} не должен быть пустым")
        if len(value) > max_length:
            raise ValueError(f"{field} не должен быть длиннее {max_length} символов")

    def validate_id(self, comment_id):
        if not isinstance(comment_id, int) or isinstance(comment_id, bool):
            raise TypeError("comment_id должен быть целым числом")

    def add(self, comment_id: int, username: str, message: str):
        self.validate_id(comment_id)
        self.validate_text(username, "username", 256)
        self.validate_text(message, "message", 8096)
        self.connection.execute(
            "INSERT INTO comments (id, name, message) VALUES (?, ?, ?)",
            (comment_id, username, message),
        )
        self.connection.commit()
        return True

    def get_by_id(self, comment_id: int):
        self.validate_id(comment_id)
        row = self.connection.execute(
            "SELECT id, name, message FROM comments WHERE id = ?", (comment_id,)
        ).fetchone()
        return dict(row) if row else None

    def get_by_name(self, username: str):
        self.validate_text(username, "username", 256)
        rows = self.connection.execute(
            "SELECT id, name, message FROM comments WHERE name = ? ORDER BY id",
            (username,),
        ).fetchall()
        return [dict(row) for row in rows]

    def update(self, comment_id: int, new_message: str):
        self.validate_id(comment_id)
        self.validate_text(new_message, "new_message", 8096)
        cursor = self.connection.execute(
            "UPDATE comments SET message = ? WHERE id = ?", (new_message, comment_id)
        )
        self.connection.commit()
        return cursor.rowcount > 0

    def delete(self, comment_id: int):
        self.validate_id(comment_id)
        cursor = self.connection.execute(
            "DELETE FROM comments WHERE id = ?", (comment_id,)
        )
        self.connection.commit()
        return cursor.rowcount > 0

    def close(self):
        self.connection.close()
