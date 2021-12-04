# Программа принимает на вход список, состоящий из других списков, и возвращает обычный список, в котором присутствуют все элементы из вложенных списков:
# Исходный список: ["Adam", ["Bob", ["Chet", "Cat"], "Bart", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# Выпрямленный список:  ['Adam', 'Bob', 'Chet', 'Cat', 'Bart', 'Bert', 'Alex', 'Bea', 'Bill', 'Ann']


def get_regular_list(lst):
    """
    Принимает на вход список, состоящий из других списков и возвращает обычный (выпрямленный список)
    
    :param lst: список
    :return: возвращает выпрямленный список
    """

    if not lst:
        return lst
    if isinstance(lst[0], list):
        return get_regular_list(lst[0]) + get_regular_list(lst[1:])
    return lst[:1] + get_regular_list(lst[1:])


lst1 = ["Adam", ["Bob", ["Chet", "Cat"], "Bart", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
print("Выпрямленный список: ", get_regular_list(lst1))
