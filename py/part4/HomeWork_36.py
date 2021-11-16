# Написать функцию, принимающую некоторую информацию о геометрической
# фигуре и рассчитывающую площадь данной фигуры.
# - Ромб с диагоналями d1 и d2 (s = (d1*d2) / 2)
# - Квадрат со стороной с (s=c2)
# - Трапеция с основаниями a,b и высотой h (s = 0.5 *(a+b)*h)
# - Круг с радиусом r (s=Pi*r2)

import math


def get_figure_square(figur, *args):
    if figur == 'rhombus':
        res = (args[0] * args[1]) / 2
        print(f'Площадь Ромба равна {res}')
    elif figur == 'square':
        res = args[0] ** 2
        print(f'Плащадь Квадрата равна {res}')
    elif figur == 'trapezoid':
        res = 0.5 * (args[0] + args[1]) * args[2]
        print(f'Площадь Трапеции равна {res}')
    elif figur == 'circle':
        res = math.pi * args[0] ** 2
        print(f'Площадь Круга равна {res}')
    else:
        print('Invalid data')


get_figure_square('rhombus', 10, 8)
get_figure_square('square', 5)
get_figure_square('trapezoid', 12, 3, 6)
get_figure_square('circle', 18)
get_figure_square('unknown', 1, 2, 3)
print()
print('1 - Ромб\n2 - Квадрат\n3 - Трапеция\n4 - Круг')
num = int(input('Выберите фигуру: '))
figure = ['rhombus', 'square', 'trapezoid', 'circle']
figure_type = 'unknown'
if 0 < num < 5:
    figure_type = figure[num - 1]
if num == 1:
    d1 = int(input('Введите диагонали:\n1 --> '))
    d2 = int(input('2 --> '))
    get_figure_square(figure_type, d1, d2)
elif num == 2:
    a = int(input('Введите сторону: '))
    get_figure_square(figure_type, a)
elif num == 3:
    a = int(input('Введите основания:\n1 --> '))
    b = int(input('2 --> '))
    h = int(input('Введите высоту: --> '))
    get_figure_square(figure_type, a, b, h)
elif num == 4:
    r = int(input('Введите радиус: --> '))
    get_figure_square(figure_type, r)
else:
    a, b, c = 1, 2, 3
    get_figure_square(figure_type, a, b, c)
