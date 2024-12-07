from django.urls import path
from .views import show_competition,filter_competition

name='surf_competition'
urlpatterns = [
    path('', show_competition),
    path('filter_competition/', filter_competition,name='filter_competition'),
]