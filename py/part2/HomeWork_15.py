# Сформировать список квадратов чисел от 1 до 10 (с помощью метода append()).

list_of_squares = []
for i in range(10):
    i += 1
    list_of_squares.append(i ** 2)
print("Список квадратов = ", list_of_squares)
