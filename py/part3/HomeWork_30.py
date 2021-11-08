# Пользователь вводит данные о количестве студентов, их фамилии, имена и балл для каждого.
# Программа должна определить средний балл и вывести фамилии и имена студентов, чей балл выше среднего

num = int(input("Введите количество студентов: "))
my_dict = {input("Введите фамилию студента: "): int(
    input("Введите баллы: ")) for i in range(num)}
print(my_dict)
score = 0
for i in my_dict:
    score += my_dict[i]
avr_score = round(score/num, 0)
print(("Средний балл:", avr_score))
print("Студенты с баллон выше среднего :", end=" ")
for key, value in my_dict.items():
    if value > avr_score:
        print(f"{key}, ", end=" ")
