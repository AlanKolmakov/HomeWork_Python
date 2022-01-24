# Создать класс "Liquid" (жидкость) со свойствами: название и плотность жидкости, —
# и методами: изменение плотности, вычисление объема жидкости, соответствующего заданной массе,
# вычисление массы жидкости, соответствующей заданному объему, вывод информации о жидкости.

# Создать произвольный класс "Alcohol" (спирт) с собственным свойством - крепость, - и методом:
# изменение крепости.

# Жидкость 'Wine' (плотность = 1064.2 kg/m^3).
# Жидкость 'Wine' (плотность = 1000 kg/m^3).

# Вес 0.5 m^3 of Wine составляет 500.0 кг.
# Объем 300 кг Wine равен 0.3 m^3.

# 14
# 20


class Liquid(object):
    def __init__(self, name: str = 'Wine', density=1064.2):
        if Liquid._check_str(name):
            self.name = name
        if Liquid._check_value(density):
            self.density = density  # плотность

    def edit_density(self, val):  # изменение плотности
        if not Liquid._check_value(val):
            print("Некорректный ввод данных плотности")
        elif val <= 0:
            print("Значения плотности должны быть больше нуля")
        else:
            self.density = val

    def calc_v(self, m):  # вычисление объема жидкости, соответствующего заданной массе
        v = round(m / self.density, 2)
        print(f"Объем {m} кг {self.name} равен {v} m^3.")
        return v

    def calc_m(self, v):  # вычисление массы жидкости, соответствующей заданному объему
        m = v * self.density
        print(f"Вес {v} m^3 {self.name} составляет {m} кг.")
        return m

    def print_info(self):  # вывод информации о жидкости
        print(f"Жидкость {self.name} (Плотность = {self.density} kg/m^3.)")

    @classmethod
    def _check_value(cls, val):
        return isinstance(val, (int, float))

    @staticmethod
    def _check_str(name):
        if isinstance(name, str):
            return True
        print("Некорректный ввод данных")


class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        if Liquid._check_value(strength):
            self.strength = strength  # крепость
        else:
            self.strength = 1

    def edit_strength(self, val):  # изменение крепости
        if Liquid._check_value(val):
            self.strength = val

    def calc_v(self, m):
        v = super().calc_v(m)
        v_alc = v * self.strength
        print(f"Объем алкоголя в {m} кг {self.name} составляет {v_alc} m^3")
        return v, v_alc

    def calc_m(self, v):
        m = super().calc_m(v)
        m_alc = m * self.strength
        print(f"Вес алкоголя {v} m^3 {self.name} составляет {m_alc} m^3")
        return m, m_alc

    def print_info(self):
        print(f"Жидкость {self.name} (Плотность = {self.density} kg/m^3.), крепость = {self.strength:.0%}")


a = Alcohol("Wine", 1064.2, 14)
a.print_info()
a.edit_density(1000)
a.print_info()
print()
a.calc_m(0.5)
a.calc_v(300)
print()
print(a.strength)
a.edit_strength(20)
print(a.strength)
