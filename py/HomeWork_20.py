# Написать функцию, принимающую некоторое целое число и вычисляющую по умолчанию
# сумму его четных цифр. Предусмотреть возможность изменения поведения функции
# таким образом, чтобы она также могла вычислять сумму нечетных цифр.
# Тестовые значения:
# N = 9874023, even_sum = 14, odd_sum = 19
# N = 38271, even_sum = 10, odd_sum = 11
# N = 123456789, even_sum = 20, odd_sum = 25


def summa(x):
    even_sum = 0
    odd_sum = 0
    for i in str(x):
        if int(i) % 2 == 0:
            even_sum += int(i)
        elif int(i) % 2 != 0:
            odd_sum += int(i)
    return even_sum, odd_sum


n1, n2, n3 = 9874023, 38271, 123456789
print(f"N = {n1}\nN = {n2}\nN = {n3}")
print(f"Сумма четных цифр:\n{summa(n1)[0]}\n{summa(n2)[0]}\n{summa(n3)[0]}")
print(f"Сумма нечетных цифр:\n{summa(n1)[1]}\n{summa(n2)[1]}\n{summa(n3)[1]}")

try:
    n = int(input("Введите число "))
    if n > 0:
        print(f"Сумма четных цифр: {summa(n)[0]}\nСумма нечетных цифр: {summa(n)[1]}")
    else:
        print(f"Некорректное число")
except ValueError:
    print("Некорректное число")
