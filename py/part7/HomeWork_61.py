# Реализуйте класс "Книга". Необходимо хранить в полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Book:
    """Класс Книга"""
    title = ""
    year = ""
    publish = ""
    genre = ""
    author = ""
    price = ""

    def print_book(self):
        print(" Информация о книги ".center(40, "*"))
        print(f"Название книги: {self.title}\nГод выпуска: {self.year}\nИздательство: {self.publish}\n"
              f"Жанр: {self.genre}\nАвтор: {self.author}\nЦена: {self.price}")
        print("=" * 40)

    def input_book(self, title, year, publish, genre, author, price):
        self.title = title
        self.year = year
        self.publish = publish
        self.genre = genre
        self.author = author
        self.price = price

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_publish(self, publish):
        self.publish = publish

    def get_publish(self):
        return self.publish

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


book1 = Book()
book1.print_book()
book1.input_book("Мара и Морок", "2021", "Эксмо", "Литературно-художественное издание", "Арден Лия", "493")
book1.print_book()
book2 = Book()
book2.set_author("Марк Лутц")
book2.set_title("Изучаем Python. Том 1")
book2.set_year("2019")
book2.set_price("2500")
book2.set_publish("Диалектика")
book2.set_genre("Научно-популярное издание")
book2.print_book()
print(book1.get_title())
print(book2.get_title())
