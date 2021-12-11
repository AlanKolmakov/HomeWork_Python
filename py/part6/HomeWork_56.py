# Есть список из 10 элементов, заполненный случайными числами. Необходимо найти число, введенное пользователем.
# Используйте алгоритм линейного поиска.
from random import randint
import time


# Вариант 1
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return True
    return False


# Вариант 2
def seq_search(lst, target):
    lst.sort()
    pos = 0
    if lst[-1] < target:
        return False
    while pos < len(lst):
        if lst[pos] == target:
            return True
        if lst[pos] > target:
            return False
        pos += 1


a = [randint(1, 100) for i in range(10)]
print(a)
n = int(input("Введите значения для поиска: "))
start = time.monotonic()
print(f'Число {n} присутствует в списке' if linear_search(a, n) else f'Число {n} в списке отсутствует')
res = time.monotonic() - start
print(round(res, 4), "sec")

print('*' * 40)
print(a)
start = time.monotonic()
print(f'Число {n} присутствует в списке' if seq_search(a, n) else f'Число {n} в списке отсутствует')
res = time.monotonic() - start
print(round(res, 4), "sec")
