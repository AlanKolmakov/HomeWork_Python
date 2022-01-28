class Student:
    """Класс Student, содержит имя и распечатывает информацию, а так же вложенный класс, который
     содержит информацию о ноутбуке с техническими характеристиками: модель, процессор и память"""
    def __init__(self, name, brand, cpu, ozu):
        self.name = name
        self.info_brand = self.Brand(brand, cpu, ozu)

    def brand_info(self):
        print(f"{self.name} => ", end="")
        self.Brand.brand_info(self.info_brand)

    class Brand:
        def __init__(self, brand, cpu, ozu):
            self.brand = brand
            self.cpu = cpu
            self.ozu = ozu

        def brand_info(self):
            print(f"{self.brand}, {self.cpu}, {self.ozu}")


s1 = Student("Roman", "HP", "i7", 16)
s2 = Student("Vladimir", "MSI", "Ryzen 5", 32)
s1.brand_info()
s2.brand_info()
