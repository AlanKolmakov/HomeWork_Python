# Поиск заданного элемента в кортеже.

a = ('ab', 'abcd', 'cde', 'abc', 'def')
s = input(f'{a}\nВведите искомый элемент: ')
print(f"{a}\ns = {s}")
for i in a:
    if s == i:
        print('Yes')
