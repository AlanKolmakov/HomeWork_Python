# Создать функцию для нахождения суммы элементов, таким образом, чтобы складывалось предыдущее значение
# с текущим произвольного количества аргументов
# 3, 9, 1  (3, 12, 13)
# 2, 5, 4, 2
# 3, 5, 10, 6, 3

def get_sum_any_args(*args):
    tmp = 0
    for i in args:
        tmp += i
        print(tmp, end=' ')
    print()


get_sum_any_args(3, 9, 1)
get_sum_any_args(2, 5, 4, 2)
get_sum_any_args(3, 5, 10, 6, 3)
