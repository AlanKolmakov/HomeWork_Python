# Дан список чисел. Выведите все элементы списка которые больше предыдущего элемента.


a = [int(input("-> ")) for i in range(int(input("Введите количество элементов списка: ")))]
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        print(a[i], end=' ')
