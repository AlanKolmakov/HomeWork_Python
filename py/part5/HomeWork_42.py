# создать функцию, которая будет находить сумму любого количества чисел и
# декоратор, который будет находить среднее арифметическое этих чисел


def sum_any_num(func):
    def wrap(*args):
        print(f'Сумма чисел {args} = {sum(args)}')
        func(sum(args), len(args), args)

    return wrap


@sum_any_num
def avr_num(x, y, z):
    print(f'Среднее арифметическое чисел {z} = {x / y}')


avr_num(2, 3, 3, 4)
