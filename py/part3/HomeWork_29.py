# Дан словарь {'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000},
# 'emp3': {'name': 'Brad', 'salary': 6500}}. Измените значение зарплаты Брэда с 6500 до 8500

my_dict = {'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000},
            'emp3': {'name': 'Brad', 'salary': 6500}}

for x in my_dict:
    print(f"{x}:")
    for y in my_dict[x]:
        print(f"\t {y}: {my_dict[x][y]}")
name = input("Введите имя: ")
the_salary = input(f"Введите новое значение зарплаты {name}: ")
for x in my_dict:
    for y in my_dict[x]:
        if my_dict[x][y] == name:
            my_dict[x]['salary'] = the_salary
            print(my_dict[x])

for x in my_dict:
    print(f"{x}:")
    for y in my_dict[x]:
        print(f"\t {y}: {my_dict[x][y]}")
