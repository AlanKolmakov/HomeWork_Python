# Написать программу, выводящую чередующиеся квадраты символов в шахматном порядке,
# пользователь вводит размер поля и количество символов

r = int(input("введите размер поля: "))
h = int(input("Введите количество символов: "))
c = 0
for n in range(r):
    c += 1
    for m in range(h):
        print()
        for i in range(h):
            if c % 2 != 0:
                for j in range(h):
                    print("*", end=" ")
                if i != j:
                    for j in range(h):
                        print(" ", end=" ")
            else:
                for j in range(h):
                    print(" ", end=" ")
                if i != j:
                    for j in range(h):
                        print("*", end=" ")
