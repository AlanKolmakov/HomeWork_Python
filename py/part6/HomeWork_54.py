# Вычислить количество отрицательных чисел в списке


def count_negative_numbers(lst):
    """
    Рекурсивная функция - возвращает количество отрицательных чисел в списке

    :param lst: список
    :return: возвращает количество отрицательных чисел в списке
    """

    if not lst:
        return 0
    else:
        count = count_negative_numbers(lst[1:])
        if lst[0] < 0:
            count += 1
        return count


lst1 = [-2, 3, 8, -11, -4, 6]
print(f"n = {count_negative_numbers(lst1)}")
