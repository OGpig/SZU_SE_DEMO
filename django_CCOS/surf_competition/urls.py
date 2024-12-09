from django.urls import path
from .views import show_competition,filter_competition,show_competition_detail

name='surf_competition'
urlpatterns = [
    path('', show_competition),
    path('filter_competition/', filter_competition,name='filter_competition'),
    path('competition_detail/', show_competition_detail,name='competition_detail'),
]