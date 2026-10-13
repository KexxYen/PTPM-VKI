import sqlite3
import logging

class Database():
    def __init__(self, db_path):
        try:
            self.connection = sqlite3.connect(db_path)
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
            self.connection.rollback()
            logging.exception("Не удалось создать таблицу triangles")

    def add_triangle(self, length1, length2, length3,triangle_type, error_message=None):    
        try:
            self.connection.execute("""
                INSERT INTO triangles (length1, length2, length3,triangle_type, error_message)
                VALUES (?, ?, ?, ?, ?)
                """,
                (length1, length2, length3,triangle_type, error_message))
            self.connection.commit()
            logging.info("Данные добавлены")
        except sqlite3.Error:
            self.connection.rollback()
            logging.exception("Не удалось добавить данные треугольника")
            

    def get(self, length1, length2, length3):
        try:
            cursor = self.connection.execute("""
                SELECT triangle_type, error_message
                FROM triangles
                WHERE length1 = ? AND length2 = ? AND length3 = ?
            """, (length1, length2, length3))
            if cursor.fetchone() is None:
                logging.info("Данные с такими параметрами не найдены")
                return 0
            logging.info("Данные получены")
            return cursor.fetchone()
        except sqlite3.Error:
            logging.exception("Не удалось получить данные треугольника")


    
    def delete(self, length1, length2, length3):
        try:
            cursor = self.connection.execute("""
                DELETE FROM triangles
                WHERE length1 = ? AND length2 = ? AND length3 = ?
            """, (length1, length2, length3))

            self.connection.commit()
            if(cursor.rowcount > 0):
                logging.info(f"Данные удалены({cursor.rowcount})")
                return cursor.rowcount
            else:
                logging.info(f"Нету данных для удаления с такими параметрами")
                return 0
            
        except sqlite3.Error:
            self.connection.rollback()
            logging.exception("Не удалось удалить данные треугольника")
            