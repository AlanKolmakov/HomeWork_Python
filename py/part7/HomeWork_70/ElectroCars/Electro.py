from attr import *
from py.part7.HomeWork_70.ElectroCars.Auto import Auto


@define(slots=True)
class ElectroCar(Auto):
    """Класс Электро автомобиль(ElectroCar) и свойством мощность батареи(pwr_battery), этот класс унаследован из
    родительского класса Автомобиль(Auto)"""
    pwr_battery: int = field(default=87, validator=validators.instance_of(int))

    @pwr_battery.validator
    def _check_pwr(self, attribute, value):
        if not value >= 0:
            raise ValueError("Значение должно быть больше 0")

    def ElectroCar_info(self):
        Auto.car_info(self)
        print(f"Автомобиль {self.full_name_car} имеет мощность батареи {self.pwr_battery} %")
