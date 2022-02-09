from dataclasses import dataclass, field
from py.part7.HomeWork_70.ElectroCars.Valid import ValidCar


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class Auto:
    """Класс Автомобиль(Auto) со свойствами бренд, модель, год выпуска и пробег. Имеет метод вывода данных на экран"""
    brand: str = ValidCar()
    model: str = ValidCar()
    year: int = ValidCar()
    mileage: int = ValidCar()
    full_name_car: str = field(init=False)

    def __post_init__(self):
        self.full_name_car = self.brand + ' ' + self.model

    def car_info(self):
        print(f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.year}\nПробег: {self.mileage} км")

