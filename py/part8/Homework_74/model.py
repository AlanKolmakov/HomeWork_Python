import pickle
import os.path


class Film:
    def __init__(self, title, genre, producer, year, duration, studio, actors, rating):
        self.title = title
        self.genre = genre
        self.producer = producer
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.genre}, {self.year}, {self.rating})"


class FilmModel:
    def __init__(self):
        self.db_name = "db.txt"
        self.films = self.load_data()  # {}

    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.films[film.title] = film

    def get_all_films(self):
        return self.films.values()

    def get_single_film(self, user_film):
        film = self.films[user_film]
        dict_film = {
            'Название': film.title,
            'Жанр': film.genre,
            'Режиссер': film.producer,
            'Год выпуска': film.year,
            'Длительность': film.duration,
            'Студия': film.studio,
            'Актеры': film.actors,
            'Рейтинг': film.rating
        }
        return dict_film

    def remove_film(self, user_film):
        return self.films.pop(user_film)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.films, f)
