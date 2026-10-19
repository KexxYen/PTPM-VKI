import logging
import sqlite3


logger = logging.getLogger(__name__)


class Database:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        try:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS triangles (
                    length1 REAL NOT NULL,
                    length2 REAL NOT NULL,
                    length3 REAL NOT NULL,
                    triangle_type TEXT NOT NULL,
                    error_message TEXT,
                    PRIMARY KEY (length1, length2, length3)
                )
            """)
            self.connection.commit()
        except sqlite3.Error:
            self.connection.close()
            raise

    def add_triangle(self, length1, length2, length3, triangle_type,
                     error_message=None):
        self.connection.execute("""
            INSERT INTO triangles
                (length1, length2, length3, triangle_type, error_message)
            VALUES (?, ?, ?, ?, ?)
        """, (length1, length2, length3, triangle_type, error_message))
        self.connection.commit()
        logger.info("Данные треугольника добавлены")
        return 1

    def get_triangle(self, length1, length2, length3):
        cursor = self.connection.execute("""
            SELECT triangle_type, error_message
            FROM triangles
            WHERE length1 = ? AND length2 = ? AND length3 = ?
        """, (length1, length2, length3))
        data = cursor.fetchone()
        if data is None:
            logger.info("Запись для заданных сторон не найдена")
        else:
            logger.info("Результат получен из БД")
        return data

    def delete_triangle(self, length1, length2, length3):
        cursor = self.connection.execute("""
            DELETE FROM triangles
            WHERE length1 = ? AND length2 = ? AND length3 = ?
        """, (length1, length2, length3))
        self.connection.commit()
        logger.info("Удалено записей: %s", cursor.rowcount)
        return cursor.rowcount

    def close(self):
        self.connection.close()
        logger.info("Соединение с БД закрыто")
