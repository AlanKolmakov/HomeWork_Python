class Clock:
    __DAY = 86400  # 24*60*60 - число секунд в одном дне

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60  # секунды
        m = (self.sec // 60) % 60  # минуты
        h = (self.sec // 3600) % 24  # часы
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __eq__(self, other):
        return self.sec == other.sec

    def __ne__(self, other):
        return self.sec != other.sec
        # return not self.__eq__(other)

    def __it__(self, other):
        return self.sec < other.sec

    def __le__(self, other):
        return self.sec <= other.sec

    def __gt__(self, other):
        return self.sec > other.sec

    def __ge__(self, other):
        return self.sec >= other.sec

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise TypeError("Ключ должен быть строкой")
        if item == "hour":
            return (self.sec // 3600) % 24
        elif item == "min":
            return (self.sec // 60) % 60
        elif item == "sec":
            return self.sec % 60
        return "Неверный ключ"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Ключ должен быть строкой")
        if not isinstance(value, int):
            raise ValueError("Значение должно быть целым числом")
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        if key == "hour":
            self.sec = s + 60 * m + value * 3600
        elif key == "min":
            self.sec = s + 60 * value + h * 3600
        elif key == "sec":
            self.sec = value + 60 * m + h * 3600


c1 = Clock(80000)
print(c1.get_format_time())  # 22:13:20
c1["hour"] = 10
c1["min"] = 55
print(c1["hour"], c1["min"], c1["sec"])  # 10:13:20
