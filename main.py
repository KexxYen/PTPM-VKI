import logging
import sqlite3

from Controller import Controller
from Database import Database
from ExternalService import FakeExternalService
from TriangleCalculate import TriangleCalculate
from UserInteraction import ConsoleUserInteraction


logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

database = None
try:
    database = Database("testing_db.db")
    user = ConsoleUserInteraction()
    calculator = TriangleCalculate()
    service = FakeExternalService()

    controller = Controller(user, calculator, database, service)
    result = controller.run()
    print("Результат:", result)
except sqlite3.Error as error:
    logging.exception("Ошибка работы с БД")
    print("Не удалось выполнить операцию с БД:", error)
finally:
    if database is not None:
        database.close()
