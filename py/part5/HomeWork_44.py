# Дан список чисел. Используя lambda-выражение, возведите в квадрат и в куб все элементы данного списка.

nums = [3, 5, 7, 3, 9, 5, 7, 2]
print(list(map(lambda x: x ** 2, nums)))
print(list(map(lambda x: x ** 3, nums)))
