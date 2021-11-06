# Дан список целых чисел. Найти минимальное среди простых чисел и
# максимальное среди чисел, не являющихся простыми.
# [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
# Min:  3
# Max:  9

def is_it_prime(k):
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False
    for a in range(3, int(k ** 0.5) + 1, 2):
        if k % a == 0:
            return False
    return True


lst = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
lst_prime = []
lst_noprime = []
for i in lst:
    if is_it_prime(i):
        lst_prime.append(i)
    else:
        lst_noprime.append(i)
print(f"{lst}\nMin:  {min(lst_prime)}\nMax:  {max(lst_noprime)}")
print(f"Список простых чисел: {lst_prime}\nСписок непростых чисел {lst_noprime}")
