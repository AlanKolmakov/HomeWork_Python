from dataclasses import dataclass
from py.part7.HomeWork_70.ElectroCars.Valid import ValidCar


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class Auto:
    """Класс Автомобиль(Auto) со свойствами бренд, модель, год выпуска и пробег. Имеет метод вывода данных на экран"""
    brand = ValidCar()
    model = ValidCar()
    year = ValidCar()
    mileage = ValidCar()
    __slots__ = ("_brand", "_model", "_year", "_mileage")
    brand: str
    model: str
    year: int
    mileage: int

    def car_info(self):
        print(f"Бренд: {self._brand}\nМодель: {self._model}\nГод выпуска: {self._year}\nПробег: {self._mileage} км")
