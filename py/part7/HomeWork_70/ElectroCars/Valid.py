class ValidCar:
    """Дескриптор задает свойства и проверяет на ввод допустимых значений"""

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.name == "_brand" or self.name == "_model" or self.name == "_full_carname":
            if isinstance(value, str):
                setattr(instance, self.name, value)
            else:
                print(f"Значение {self.name} должно быть строкой")
        if self.name == "_year" or self.name == "_mileage" or self.name == "_pwr_battery":
            if isinstance(value, int) and value > 0:
                setattr(instance, self.name, value)
            else:
                print(f"Значение {self.name} должно быть целым положительным числом")
