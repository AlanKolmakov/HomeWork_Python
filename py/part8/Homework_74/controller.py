from view import UserInterface
from model import FilmModel


class Controller:
    def __init__(self):
        self.film_model = FilmModel()  # model
        self.user_interface = UserInterface()  # view

    def run(self):
        answer = None
        while answer != 'q' and answer != 'й':
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        match answer:
            case "1":
                film = self.user_interface.add_user_film()
                self.film_model.add_film(film)
            case "2":
                films = self.film_model.get_all_films()
                self.user_interface.show_all_films(films)
            case "3":
                film_title = self.user_interface.get_user_film()
                try:
                    film = self.film_model.get_single_film(film_title)
                except KeyError:
                    self.user_interface.show_incorrect_error(film_title)
                else:
                    self.user_interface.show_single_film(film)
            case "4":
                film_title = self.user_interface.get_user_film()
                try:
                    title = self.film_model.remove_film(film_title)
                except KeyError:
                    self.user_interface.show_incorrect_error(film_title)
                else:
                    self.user_interface.remove_single_film(title)
            case "q" | "й":
                self.film_model.save_data()
            case _:
                self.user_interface.show_incorrect_answer_error(answer)
