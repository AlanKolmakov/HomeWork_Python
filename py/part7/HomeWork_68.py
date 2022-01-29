import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Класс Shape и три дочерних класса: Square, Rectangle, Triangle. Родительский класс имеет
    абстрактные методы нахождения периметра, площади, рисования фигуры и вывода информации.
    Реализован вывод информации о дочерних классах с помощью полиморфизма."""
    @abstractmethod
    def perimetr(self):
        print("abstract method perimetr must be implemented in child classes!!!")

    @abstractmethod
    def sqr(self):
        print("abstract method sqr must be implemented in child classes!!!")

    @abstractmethod
    def draw(self):
        print("abstract method draw must be implemented in child classes!!!")

    @abstractmethod
    def print_info(self):
        print("abstract method print_info must be implemented in child classes!!!")

    @staticmethod
    def _int_verify(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")

    @staticmethod
    def _str_verify(value):
        if not isinstance(value, str):
            raise TypeError("Значение должно быть строкой")


class Square(Shape, ABC):
    __slots__ = '__side', '__color'

    def __init__(self, side, color: str = "red"):
        self.side = side
        self.color = color

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        self._int_verify(side)
        self.__side = side

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self._str_verify(color)
        self.__color = color

    def perimetr(self):  # Периметр
        return self.side * 4

    def sqr(self):  # Площадь
        return self.side ** 2

    def draw(self):  # Рисование фигуры
        for i in range(self.side):
            print("*" * self.side)

    def print_info(self):
        print(f"Квадрат".center(13, "="))
        print(f"Сторона: {self.side}\nЦвет: {self.color}\nПлощадь: {self.sqr()}\nПериметр: {self.perimetr()}")
        self.draw()


class Rectangle(Shape, ABC):
    __slots__ = '__length', '__width', '__color'

    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self._int_verify(length)
        self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self._int_verify(width)
        self.__width = width

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self._str_verify(color)
        self.__color = color

    def perimetr(self):  # Периметр P = 2 * (l + w)
        return (self.length + self.width) * 2

    def sqr(self):  # Площадь S = a × b
        return self.length * self.width

    def draw(self):  # Рисование фигуры
        for i in range(self.length):
            print("*" * self.width)

    def print_info(self):
        print(f"Прямоугольник".center(19, "="))
        print(f"Длина: {self.length}\nШирина: {self.width}\nЦвет: {self.color}\nПлощадь: {self.sqr()}"
              f"\nПериметр: {self.perimetr()}")
        self.draw()


class Triangle(Shape, ABC):
    __slots__ = '__side1', '__side2', '__side3', '__color'

    def __init__(self, side1, side2, side3, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.color = color

    @property
    def side1(self):
        return self.__side1

    @side1.setter
    def side1(self, side1):
        self._int_verify(side1)
        self.__side1 = side1

    @property
    def side2(self):
        return self.__side2

    @side2.setter
    def side2(self, side2):
        self._int_verify(side2)
        self.__side2 = side2

    @property
    def side3(self):
        return self.__side3

    @side3.setter
    def side3(self, side3):
        self._int_verify(side3)
        self.__side3 = side3

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self._str_verify(color)
        self.__color = color

    def perimetr(self):  # Периметр P = (a + b + c)/2
        return (self.side1 + self.side2 + self.side3) / 2

    def sqr(self):  # Площадь
        p = self.perimetr()
        return round(math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3)), 2)

    def draw(self):  # Рисование фигуры
        for i in range(1, self.side2 * 2, 2):
            print(('*' * i).center(self.side2 * 2))

    def print_info(self):
        print(f"Треугольник".center(17, "="))
        print(f"Сторона 1: {self.side1}\nСторона 2: {self.side2}\nСторона 3: {self.side3}\nЦвет: {self.color}\n"
              f"Площадь: {self.sqr()}\nПериметр: {self.perimetr()}")
        self.draw()


p1 = Square(3, "red")
p2 = Rectangle(3, 7, "green")
p3 = Triangle(11, 6, 6, "yellow")
s = [p1, p2, p3]
for r in s:
    r.print_info()
    print()
