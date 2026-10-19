import logging
from abc import ABC, abstractmethod


logger = logging.getLogger(__name__)


class UserInteraction(ABC):
    @abstractmethod
    def get_data(self):
        pass

class ConsoleUserInteraction(UserInteraction):
    def get_data(self):
        while True:
            try:
                a = float(input("Введите первую сторону: "))
                b = float(input("Введите вторую сторону: "))
                c = float(input("Введите третью сторону: "))
                logger.debug("Получены стороны: %s, %s, %s", a, b, c)
                return a, b, c
            except ValueError:
                logger.warning("Пользователь ввёл некорректное число")
                print("Ошибка: введите числа. Повторите ввод.")
