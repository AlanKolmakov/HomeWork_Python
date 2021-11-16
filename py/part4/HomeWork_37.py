# Решить квадратное уравнение 2x^2+3*x-5=0

# a * x ** 2 + b * x + c =0

import math
a, b, c = 2, 3, -5
d = b**2 - 4 * a * c
res = [(-b - math.sqrt(d)) / (2 * a), (-b + math.sqrt(d)) / (2 * a)]
print(res)
