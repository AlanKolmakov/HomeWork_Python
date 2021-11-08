# Создать функцию для нахождения минимального значения произвольного количества аргументов
def get_min_any_count_args(*args):
    return min(args)


print(get_min_any_count_args(10, 9))
print(get_min_any_count_args(2, 3, 4))
print(get_min_any_count_args(3, 5, 10, 6))
