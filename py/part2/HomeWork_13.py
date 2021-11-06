# Напишите программу заполнения списка положительными и отрицательными элементами.
# Из него требуется сформировать новый массив только из положительных элементов.
# Найти из них наибольший элемент. Распечатать новый массив и наибольший элемент

def choice_sort(a):
    """ сортироовка списка а выбором """
    n = len(a)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]
    return a


user_list = []
new_positive_elements = []
while True:
    print("Для выхода из программы введите 'q'")
    num = input("Введите элемент списка: ")
    if num == "q":
        input("Выход из программы\n\nНажмите любую клавишу")
        break
    try:
        num = int(num)
    except ValueError:
        print("Вы не ввели число")
        continue
    user_list.append(num)
    if num > 0:
        new_positive_elements.append(num)
    print("Список: ", user_list)
    print("Новый список, состоящий из положительных элементов: ",
        new_positive_elements)
    print("Наибольший элемент списка: ", max(user_list))
    print("Сортированный список: ", choice_sort(user_list), "\n\n\n")
