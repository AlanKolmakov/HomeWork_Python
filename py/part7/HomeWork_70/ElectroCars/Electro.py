from dataclasses import dataclass
from py.part7.HomeWork_70.ElectroCars.Auto import Auto
from py.part7.HomeWork_70.ElectroCars.Valid import ValidCar


@dataclass()
class ElectroCar(Auto):
    """Класс Электро автомобиль(ElectroCar) и свойством мощность батареи(pwr_battery), этот класс унаследован из
    родительского класса Автомобиль(Auto)"""
    pwr_battery: int = ValidCar()

    def ElectroCar_info(self):
        Auto.car_info(self)
        print(f"Автомобиль {self.full_name_car} имеет мощность батареи {self.pwr_battery} %")
