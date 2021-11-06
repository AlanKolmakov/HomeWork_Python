# Написать функцию, принимающую произвольное количество целых чисел
# и возвращающую наибольшее положительное из них кратное 13


def get_max_multiple_13(num):
    x = num.copy()
    x.sort()
    for i in reversed(x):
        if i % 13 == 0 and i > 0:
            print(f"Наибольшее кратное 13: {num}\n{i}\n")
            return num
    print(f"Наибольшее кратное 13: {num}\nНет таких чисел\n")


test1 = [2, 7, 0, 3, 1, 5, -13]
test2 = [2, 7, 0, 3, 1, 5, -13, 13]
test3 = [26]
test4 = [99, 99, 100, 34, -39]
test5 = [99, 39, 99, 100, 34]
get_max_multiple_13(test1)
get_max_multiple_13(test2)
get_max_multiple_13(test3)
get_max_multiple_13(test4)
get_max_multiple_13(test5)

nums = []
while True:
    print("Для завершения ввода введите любую букву")
    try:
        nums.append(
            int(input("\nВведите произвольное количество целых чисел: ")))
        print(nums)
    except ValueError:
        if len(nums) == 0:
            print("Вы не ввели ни одного числа")
            continue
        break
get_max_multiple_13(nums)
