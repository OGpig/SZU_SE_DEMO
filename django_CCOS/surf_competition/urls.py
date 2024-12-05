from django.urls import path
from .views import show_competition

name='surf_competition'
urlpatterns = [
    path('surf_competition/', show_competition),
]