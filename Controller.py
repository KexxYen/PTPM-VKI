import logging


logger = logging.getLogger(__name__)


class Controller:
    def __init__(self, user, calculator, database, external_service):
        self.user = user
        self.calculator = calculator
        self.database = database
        self.external_service = external_service

    def run(self):
        a, b, c = self.user.get_data()
        saved_result = self.database.get_triangle(a, b, c)

        if saved_result is None:
            triangle_type, _, error_message = self.calculator.calculate(a, b, c)
            self.database.add_triangle(a, b, c, triangle_type, error_message)
            logger.info("Новый результат рассчитан и сохранён")
        else:
            triangle_type, error_message = saved_result
            logger.info("Использован сохранённый результат")

        message = f"Тип треугольника: {triangle_type}"
        if error_message is not None:
            message += f". {error_message}"

        self.external_service.send(message)
        return message
