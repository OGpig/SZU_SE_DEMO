from django.urls import path
from .views import show_competition

name = 'home_page'

urlpatterns = [
    path('home_page/', show_competition),
]