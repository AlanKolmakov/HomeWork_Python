# Написать функцию перевод десятичного числа в двоичное


def decToBin(n):
    """
    Перевод десятичного числа в двоичное

    :param n: любое положительное число
    :return: возвращает число в двоичном коде
    """

    b = ""
    try:
        n = int(n)
        while n > 0:
            b = str(n % 2) + b
            n = n // 2
        return b
    except ValueError:
        return n


print(decToBin(53))
print(decToBin(145))
print(decToBin(255))
num = 1
while num > 0:
    print("Для выхода введите любое отрицательное число")
    try:
        num = int(input("Введите число, которое хотите перевести в двоичное: "))
        print(decToBin(num))
    except ValueError:
        pass
