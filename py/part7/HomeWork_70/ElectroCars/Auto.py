from attr import *


@define(slots=True)
class Auto:
    """Класс Автомобиль(Auto) со свойствами бренд, модель, год выпуска и пробег. Имеет метод вывода данных на экран"""
    brand: str = field(default="Tesla", validator=validators.instance_of(str))
    model: str = field(default="T", validator=validators.instance_of(str))
    year: int = field(default=2018, validator=validators.instance_of(int))
    mileage: int = field(default=99000, validator=validators.instance_of(int))
    full_name_car: str = field(init=False)

    def __attrs_post_init__(self):
        if self.mileage < 0:
            self.mileage *= -1
        self.full_name_car = self.brand + ' ' + self.model

    def car_info(self):
        print(f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.year}\nПробег: {self.mileage} км")
