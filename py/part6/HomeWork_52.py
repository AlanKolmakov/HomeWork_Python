import re

# Валидация номера телефона


def validate_phone_number(value):
    """
    Проверяет строку на валидность номера телефона

    :param value: строка
    :return: возвращает True если номер телефона соответствует шаблону, если нет возвращает False
    """
    reg = r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'
    result = re.findall(reg, value)
    print(f'{value} - {bool(result)}')
    return bool(result)


validate_phone_number('9041469275')
validate_phone_number('5041469275')
validate_phone_number('+74994564578')
validate_phone_number('+7499456.4578')
validate_phone_number('7 (499) 456-45 78')
validate_phone_number('7 (499) 456*45 78')
validate_phone_number('7 (499) 456-45 785')
validate_phone_number('+9 (499) 456-45 78')
validate_phone_number('8 (499) 4564543')
validate_phone_number('6 (499) 4564543')
validate_phone_number('6 &(499) 4564543')


def validate_phone(value):
    """
    Проверяет строку на наличие номера телефона и строгое соответствие шаблону:
    +7хххххххххх или 7xxxxxxxxxx или 8хххххххххх
    :param value: строка
    :return: возвращает True если номер телефона соответствует шаблону, если нет возвращает False
    """
    reg = r'^(\+7?|7|8)\d{10}$'
    result = re.findall(reg, value)
    print(f'{value} - {bool(result)}')
    return bool(result)


validate_phone('+7 904 146-92-75')
validate_phone('+74994564578')
validate_phone('7 (499) 456 45 78')
validate_phone('8 (499) 4564543')
