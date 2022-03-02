def add_film(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50, "\n")
            return output
        return wrap
    return wrapper


class UserInterface:
    @add_film('Редактирование данных каталога фильмов')
    def wait_user_answer(self):
        print("Действия с фильмами:")
        print("1 - Добавление фильмов"
              "\n2 - Каталог фильмов"
              "\n3 - Просмотр определенного фильма"
              "\n4 - Удаление фильма"
              "\nq - Выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_film('Добавить фильм:')
    def add_user_film(self):
        dict_film = {
            'Название': None,
            'Жанр': None,
            'Режиссер': None,
            'Год выпуска': None,
            'Длительность': None,
            'Студия': None,
            'Актеры': None,
            'Рейтинг': None
        }
        for key in dict_film:
            dict_film[key] = input(f"{key}: ")
        return dict_film

    @add_film('Список фильмов')
    def show_all_films(self, films):
        for ind, film in enumerate(films, start=1):
            print(f"{ind}. {film}")

    @add_film('Ввод названия фильма:')
    def get_user_film(self):
        user_film = input("Введите название фильма: ")
        return user_film

    @add_film('Просмотр фильма:')
    def show_single_film(self, film):
        for key in film:
            print(f"{key} фильма - {film[key]}")

    @add_film('Сообщение об ошибке:')
    def show_incorrect_error(self, user_title):
        print(f"Фильм с названием {user_title} не существует")

    @add_film('Удаление фильма:')
    def remove_single_film(self, film):
        print(f"Фильм {film} - был удален")

    @add_film('Сообщение об ошибке:')
    def show_incorrect_answer_error(self, answer):
        print(f"Вариант {answer} не существует")