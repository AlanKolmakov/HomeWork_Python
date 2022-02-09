from py.part7.HomeWork_70.ElectroCars.Electro import *

car1 = ElectroCar("Tesla", "T", 2018, 99000, 87)
car2 = ElectroCar("Mitsubishi", "i-MiEV", 2020, 20000, 98)
cars_lst = [car1, car2]
for i in cars_lst:
    i.ElectroCar_info()
    print("==" * 40)

