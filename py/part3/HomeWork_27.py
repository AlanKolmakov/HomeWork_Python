# Вывод уникальных букв из двух строк.

a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")
a = list(set(a) ^ set(b))
print("Искомыми буквами являются: ")
for i in a:
    print(i, end=' ')
