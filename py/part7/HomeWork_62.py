# Разработать класс Sphere для предоставления сферы в трехмерном пространстве. Создать в классе набор методов:
# - get_volume() должен возвращать действительное число - объем шара, ограниченной текущей сферой.
# - get_square() должен возвращать действительное число - площадь внешней поверхности сферы.
# - get_radius() должен возвращать действительное число - радиус сферы.
# - get_center(), должен возвращать кортеж с 3 действительными числами - координатами центра сферы в том же порядке,
# в каком они задаются в инициализаторе.
# - set_radius(r) должен принимать 1 аргумент - действительное число, и меняет радиус текущей сферы, ничего не возвращая
# - set_center(x, y, z) должен принимать 3 аргумента - действительные числа, и менять координаты центра сферы,
# ничего не возвращая. Координаты задаются в том же порядке, что и в инициализаторе.
# - is_point_inside(x, y, z) должен принимать 3 аргумента - действительные числа - координаты некоторой точки в
# пространстве (в том числе порядке, что и в инициализаторе), и возвращать логическое значение True или False
# в зависимости от того, находится эта точка внутри сферы.
from math import pi


class Sphere:
    """Класс Sphere для предоставления сферы в трехмерном пространстве"""
    def __init__(self, r=1, x=0, y=0, z=0):
        self.__r, self.__x, self.__y, self.__z = r, x, y, z

    def __is_digit(num):
        return isinstance(num, (int, float))

    def set_radius(self, r):
        if Sphere.__is_digit(r):
            if r > 0:
                self.__r = r
        else:
            print("Некорректные данные радиуса")

    def set_center(self, x, y, z):
        if Sphere.__is_digit(x) and Sphere.__is_digit(y) and Sphere.__is_digit(z):
            self.__x, self.__y, self.__z = x, y, z

    def get_volume(self):
        return (self.__r ** 3) * pi * 4 / 3

    def get_square(self):
        return (self.__r ** 2) * pi * 4

    def get_radius(self):
        return self.__r

    def get_center(self):
        return self.__x, self.__y, self.__z

    def is_point_inside(self, x, y, z):
        if Sphere.__is_digit(x) and Sphere.__is_digit(y) and Sphere.__is_digit(z):
            return (self.__x - x) ** 2 + (self.__y - y) ** 2 + (self.__z - z) ** 2 <= self.__r ** 2
        else:
            print("Некорректные данные координат")


p1 = Sphere()
p1.set_radius("0.6")
p1.set_radius(0.6)
print(f"get_radius: {p1.get_radius()}")
print(f"get_volume: {p1.get_volume()}")
print(f"get_square: {p1.get_square()}")
print(f"get_center: {p1.get_center()}")
print(f"get_square: {p1.get_square()}")
p1.is_point_inside("0", -1.5, 0)
print(f"is_point_inside: {p1.is_point_inside(0, -1.5, 0)}")
p1.set_radius(1.6)
print(f"set_radius: {p1.get_radius()}")
print(f"is_point_inside: {p1.is_point_inside(0, -1.5, 0)}")
