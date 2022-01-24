import math
from abc import ABC, abstractmethod


class Root(ABC):
    """Абстрактный класс 'Корень' с методами вычисления корней уравнения и вывода результата на экран."""
    count = 0

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        Root.count += 1

    @abstractmethod
    def calc_roots(self):
        print("abstract method calc_roots must be implemented in child classes!!!")

    @staticmethod
    def __check_value(v):
        return isinstance(v, (int, float))

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.__check_value(value):
            self.__x = value
        else:
            print("Значения x не должно быть строкой")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.__check_value(value):
            self.__y = value
        else:
            print("Значения y не должно быть строкой")

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, value):
        if self.__check_value(value):
            self.__z = value
        else:
            print("Значения z не должно быть строкой")


class LinearRoot(Root):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

    def calc_roots(self):
        res = round(-self.y / self.x, 2)
        print(f"The root of '{self.x}x+{self.y}=0' is: {res}")


class SquareRoot(Root):

    def calc_roots(self):
        res = self.y ** 2 - self.x * self.z * 4
        s1 = round((-self.y + math.sqrt(res)) / (2 * self.x), 2)
        s2 = round((-self.y - math.sqrt(res)) / (2 * self.x), 2)
        print(f"The roots of '{self.x}x^2{self.y}x{self.z}=0' are: {s1}, {s2}")


r1 = LinearRoot(3, 7)
r1.calc_roots()
print()
r2 = SquareRoot(1, -2, -3)
r2.calc_roots()
print()
print(f"Number of calls: {Root.count}")
