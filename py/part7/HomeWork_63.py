# Создайте класс для конвертирования температуры из Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейт в Цельсий. Также
# класс должен считать количество подсчетов температуры и возвращать это значение с помощью статического метода.

class ConvertTemperature:
    count = 0
    suffix_C = u'\xb0C'
    suffix_F = u'\xb0F'

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        if ConvertTemperature.check_value(celsius, True):
            ConvertTemperature.count += 1
            return (f'{celsius}{ConvertTemperature.suffix_C} = {round((celsius * 1.8) + 32, 2)}'
                    f'{ConvertTemperature.suffix_F}')
        return "Некорректный ввод данных"

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        if ConvertTemperature.check_value(fahrenheit, False):
            ConvertTemperature.count += 1
            return (f'{fahrenheit}{ConvertTemperature.suffix_F} = {round((fahrenheit - 32) / 1.8, 2)}'
                    f'{ConvertTemperature.suffix_C}')
        return "Некорректный ввод данных"

    @staticmethod
    def get_count():
        return f'Количество подсчетов температуры: {ConvertTemperature.count}'

    def check_value(self, flag):
        if flag:
            if isinstance(self, (int, float)) and self > -273:
                return True
        if not flag:
            if isinstance(self, (int, float)) and self > -459.4:
                return True
        return False


print(ConvertTemperature.get_count())
print(ConvertTemperature.celsius_to_fahrenheit("-300"))
print(ConvertTemperature.celsius_to_fahrenheit(15))
print(ConvertTemperature.fahrenheit_to_celsius(-500))
print(ConvertTemperature.fahrenheit_to_celsius(59))
print(ConvertTemperature.get_count())
