# Вычислите площадь треугольника по сторонам и углу между ними
import math


def triangle(a, b, c):
    s = 0.5 * ((a * b) * math.sin(math.radians(c)))
    return s


side1 = int(input("Сторона 1: "))
side2 = int(input("Сторона 2: "))
angle = int(input("Угол: "))
print("Плащадь треугольника: ", triangle(side1, side2, angle))
