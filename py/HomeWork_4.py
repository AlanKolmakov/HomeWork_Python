# Написать программу "калькулятор"

while True:
    print("простейшая программа калькулятор\n")
    print("Выберите операцию:\n1 - 'r' - применяет унарный минус к операнду\n"
        "2 - '+' - сложение\n3 - '-' - вычитание\n4 - '/' - деление\n5 - '*' - умножение\n"
        "6 - '%' - деление по модулю (остаток от деления)\n7 - '<' - минимальное из двух чисел\n"
        "8 - '>' - максимальное из двух чисел\nq -       Выход из программы")
    user_choice = input("Введите цифру: ")
    if user_choice == "q":
        break
    user_choice = int(user_choice)
    result = ""
    if user_choice == 1:
        num1 = float(input("Введите число: "))
        result = -num1
    elif user_choice == 6:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите модуль числа: "))
        result = f"Остаток от деления числа {num1} по модулю {num2} равен", num1 % num2
    elif 1 <= user_choice <= 8:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        if user_choice == 2:
            result = num1 + num2
        elif user_choice == 3:
            result = num1 - num2
        elif user_choice == 4:
            if num2 == 0:
                print("На ноль делить нельзя!!!\n\nВыход из программы")
                break
            else:
                result = num1 / num2
        elif user_choice == 5:
            result = num1 * num2
        elif user_choice == 7:
            if num1 < num2:
                print(f"Минимальное число {num1}")
            elif num1 > num2:
                print(f"Минимальное число {num2}")
            else:
                print(f"{num1} равно {num2}")
            break
        elif user_choice == 8:
            if num1 > num2:
                print(f"Максимальное число {num1}")
            elif num1 < num2:
                print(f"Максимальное число {num2}")
            else:
                print(f"{num1} равно {num2}")
            break
        if result.is_integer():
            result = int(result)
    else:
        print("Ошибка ввода")
    print(result)
