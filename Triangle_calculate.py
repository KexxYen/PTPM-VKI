import logging
import math

class TriangleCalculate:
    def calculate(self, length1, length2, length3):
        self.a = length1
        self.b = length2
        self.c = length3 

        if self.a <= 0 or self.b <= 0 or self.c <= 0 or not math.isfinite(self.a) or not math.isfinite(self.b) or not math.isfinite(self.c):
            logging.warning("Ошибка: стороны должны быть положительными конечными числами")
            coordinates = [(-1, -1), (-1, -1), (-1, -1)]
            return "не треугольник", coordinates

        sides = sorted([self.a, self.b, self.c])
        longest = sides[2]
        small = sides[0] / longest
        middle = sides[1] / longest


        if small <= 1 - middle:
            logging.warning("Ошибка: сумма двух сторон должна быть больше третьей")
            coordinates = [(-1, -1), (-1, -1), (-1, -1)]
            return "не треугольник", coordinates 

        if self.a == self.b and self.b == self.c: 
            triangle_type = "равносторонний"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            triangle_type = "равнобедренный"
        else:
            triangle_type = "разносторонний"

        x = (middle * middle + 1 - small * small) / 2
        y = math.sqrt(max(0, middle * middle - x * x))

        A = (10, 10)
        B = (90, 10)
        C = (int(x * 80) + 10, int(y * 80) + 10)

        return triangle_type, [A, B, C]