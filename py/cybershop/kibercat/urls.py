from django.urls import path
from .views import *


urlpatterns = [
    path('', KibercatMainPage.as_view(), name='main'),
]