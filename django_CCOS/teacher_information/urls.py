from django.urls import path
from .views import show_competition

name = 'teacher_information'

urlpatterns = [
    path('', show_competition),
]