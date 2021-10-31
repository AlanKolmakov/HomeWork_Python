import math

# Напишите функции нахождения площади фигур:


def area(figur, a, b):
    if figur == 1:
        return a * b
    if figur == 2:
        return (a * b) / 2
    if figur == 3:
        return math.pi * (a ** 2)


while True:
    print(f"Выберете фигуру:\n 1) Прямоугольник\n 2) Треугольник\n 3) Круг")
    figur = int(input("---> "))
    if figur == 1:
        name = "Прямоугольника"
        x = int(input("Длина: "))
        y = int(input("Ширина: "))
        break
    elif figur == 2:
        name = "Треугольника"
        x = int(input("Основание: "))
        y = int(input("Высота: "))
        break
    elif figur == 3:
        name = "Круга"
        x = int(input("Радиус: "))
        y = 0
        break
    else:
        print("Вы должны ввести целое число от 1 до 3\n")
        continue
print(f"Площадь {name} равна = {area(figur, x, y)}")

# Прямоугольник:
# Для вычисления необходимо умножить их друг на друга. S = a × b, где S — площадь; a, b — длина и ширина.
#
# Треугольник:
# S = 0,5 * a * h, где a — основание, h — высота.
