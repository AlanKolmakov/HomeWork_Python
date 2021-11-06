# Разработать программу, которая выводит на экран линию из символов.
# Пользователь указывает: число символов, тип символа,
# и ориентацию линии - вертикальную или горизонтальную

num_symbol = int(input("Введите количество символов: "))
type_symbol = str(input("Введите тип символа: "))
user_choice = int(input("0 - горизонтальная\n1 - вертикальная:\t"))
for i in range(num_symbol):
    if user_choice == 0:
        print(type_symbol, end=" ")
    else:
        print(type_symbol)
