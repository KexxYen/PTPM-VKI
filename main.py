import logging
import math
import sys
from pathlib import Path

def main():
    logs_folder = Path(__file__).parent / "logs"
    logs_folder.mkdir(exist_ok=True)

    logging.basicConfig(
        level=logging.info,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(logs_folder / "file_txt.log", encoding="utf-8")
        ]
    )
    logging.info("Приложение запущено")

    a = b = c = "не введено"
    try:
        a = input("Введите A: ")
        b = input("Введите B: ")
        c = input("Введите C: ")

        logging.info("Запрос: A=%r, B=%r, C=%r", a, b, c)
        triangle_type, coordinates = calc_triangle(a, b, c)
    except Exception:
        logging.exception("Ошибка выполнения: A=%r, B=%r, C=%r", a, b, c)
        print("Не удалось обработать данные.")
        return

    if triangle_type == "" or triangle_type == "не треугольник":
        logging.warning("Запрос отклонён: A=%r, B=%r, C=%r; тип=%r; координаты=%s",
                        a, b, c, triangle_type, coordinates)
    else:
        logging.info("Успешный запрос: A=%r, B=%r, C=%r; тип=%s; координаты=%s",
                     a, b, c, triangle_type, coordinates)

    print("\nРезультат:")
    print("Тип треугольника:", triangle_type)
    print("Координаты:", coordinates)


def calc_triangle(a, b, c):
    try: 
        a = float(a)
        b = float(b)
        c = float(c)
    except (ValueError, TypeError):
        logging.warning("Ошибка: все стороны должны быть числами")
        coordinates = [(-2, -2), (-2, -2), (-2, -2)]
        return "", coordinates
   
    if a <= 0 or b <= 0 or c <= 0 or not math.isfinite(a) or not math.isfinite(b) or not math.isfinite(c):
        logging.warning("Ошибка: стороны должны быть положительными конечными числами")
        coordinates = [(-1, -1), (-1, -1), (-1, -1)]
        return "не треугольник", coordinates

    sides = sorted([a, b, c])
    longest = sides[2]
    small = sides[0] / longest
    middle = sides[1] / longest


    if small <= 1 - middle:
        logging.warning("Ошибка: сумма двух сторон должна быть больше третьей")
        coordinates = [(-1, -1), (-1, -1), (-1, -1)]
        return "не треугольник", coordinates 

    if a == b and b == c: 
        triangle_type = "равносторонний"
    elif a == b or a == c or b == c:
        triangle_type = "равнобедренный"
    else:
        triangle_type = "разносторонний"

    x = (middle * middle + 1 - small * small) / 2
    y = math.sqrt(max(0, middle * middle - x * x))

    A = (10, 10)
    B = (90, 10)
    C = (int(x * 80) + 10, int(y * 80) + 10)

    return triangle_type, [A, B, C]


if __name__ == "__main__":
    main()
