# Написать функцию, которая принимает один аргумент, который в дальнейшем будет умножаться на заданное число.

def func_compute(n):
    return lambda x: x * n


res = func_compute(2)
print(res(15))
print(res(20))
res = func_compute(3)
print(res(15))
print(res(20))
