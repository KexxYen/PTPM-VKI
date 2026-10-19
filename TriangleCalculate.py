import logging
import math


logger = logging.getLogger(__name__)


class TriangleCalculate:
    def calculate(self, length1, length2, length3):
        a, b, c = length1, length2, length3

        if (not all(math.isfinite(side) for side in (a, b, c))
                or min(a, b, c) <= 0):
            error_message = "Ошибка: стороны должны быть положительными конечными числами"
            logger.warning(error_message)
            return "не треугольник", [(-1, -1)] * 3, error_message

        sides = sorted((a, b, c))
        longest = sides[2]
        small = sides[0] / longest
        middle = sides[1] / longest

        if small <= 1 - middle:
            error_message = "Ошибка: сумма двух сторон должна быть больше третьей"
            logger.warning(error_message)
            return "не треугольник", [(-1, -1)] * 3, error_message

        if a == b == c:
            triangle_type = "равносторонний"
        elif a == b or a == c or b == c:
            triangle_type = "равнобедренный"
        else:
            triangle_type = "разносторонний"

        x = (middle * middle + 1 - small * small) / 2
        y = math.sqrt(max(0, middle * middle - x * x))
        coordinates = [(10, 10), (90, 10),
                       (int(x * 80) + 10, int(y * 80) + 10)]
        logger.info("Вычислен тип треугольника: %s", triangle_type)
        return triangle_type, coordinates, None
