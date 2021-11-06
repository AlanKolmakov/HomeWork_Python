# Дан список целых чисел, число k и значение c. Необходимо вставить в список на позицию
# c индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.

num_list = []
num_count = int(input("Введите элементы списка: "))
for i in range(num_count):
    num_list.append(int(input("-> ")))
k = int(input("Введите индекс: "))
print("k = ", k)
c = int(input("Введите значение: "))
print("c = ", c)
num_list.insert(k, c)
print(num_list)
