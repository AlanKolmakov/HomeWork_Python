from django.shortcuts import render
from django.views.generic import ListView

from .models import *

menu = [
    {'index_name': 'Контакты', 'url_name': 'main'},
    {'index_name': 'Доставка и оплата', 'url_name': 'main'},
    {'index_name': 'Гарантия и возврат', 'url_name': 'main'},
    {'index_name': 'Бренды', 'url_name': 'main'},
    {'index_name': 'Подобрать кресло', 'url_name': 'main'},
    {'index_name': 'Задайте вопрос', 'url_name': 'main'},
    {'index_name': 'Личный кабинет', 'url_name': 'main'},
]


class KibercatMainPage(ListView):
    model = Product
    template_name = 'kibercat/main.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'Киберспортивный магазин для геймеров KiberCat.ru'
        content['menu'] = menu
        return content
