# Создать класс "Треугольник", свойства - длины трех сторон. Правильность задания свойств должны проверяться
# через дескриптор на ввод положительных целых числовых значений. Предусмотреть в классе методы
# проверки существования треугольника
#
# Треугольник со сторонами (2, 5, 6) существует
# Треугольник со сторонами (5, 2, 8) не существует
# Треугольник со сторонами (7, 3, 9) существует

class ValidIntTriangle:
    """Дескриптор задает свойства и проверяет на ввод положительных целых значений"""
    @classmethod
    def verify_int(cls, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError(f"Значение {value} должно быть целым положительным числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_int(value)
        setattr(instance, self.name, value)


class Triangle:
    """Класс "Треугольник", свойства - длины трех сторон и метод проверки существования треугольника."""
    x = ValidIntTriangle()
    y = ValidIntTriangle()
    z = ValidIntTriangle()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def verifyIsTriangle(self):
        if (self.x + self.y) > self.z and (self.x + self.z) > self.y and (self.y + self.z) > self.x:
            print(f" Треугольник со сторонами {self.x}, {self.y} и {self.z} существует")
        else:
            print(f" Треугольник со сторонами {self.x}, {self.y} и {self.z} не существует")


t1 = Triangle(2, 5, 6)
t2 = Triangle(5, 2, 8)
t3 = Triangle(7, 3, 9)
lst = [t1, t2, t3]
for i in lst:
    i.verifyIsTriangle()
    # print(i.__dict__)
