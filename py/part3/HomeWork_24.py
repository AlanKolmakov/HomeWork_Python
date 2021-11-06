# найдите все буквы в первой строке, которые отсутствуют во второй.

set1 = set(input("Введите первую строку: "))
set2 = set(input("Введите вторую строку: "))
set1.difference_update(set2)
for i in set1:
    print(i, end=' ')
print()

# без использования множеств
print(' '.join([i for i in set1 if i not in set2]))
