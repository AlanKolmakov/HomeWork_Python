# Удаление буквы из слова, заданной номером позиции


def Delete_Chart_Pos(x, num_pos):
    """
    Удаление буквы из слова

    Удаление буквы из слова, заданной номером позиции
    :param x: строка, из которой удаляется символ
    :param num_pos: позиция символа в удаляемой строке x
    :return: возвращает строку через срез с удаленной позицией
    """
    if (num_pos < 0) or (num_pos >= len(s)):
        return x

    return x[:num_pos] + x[num_pos + 1:]


s = "0123456789"
s2 = Delete_Chart_Pos(s, 4)
print("s =  ", s)
print("s2 = ", s2)
