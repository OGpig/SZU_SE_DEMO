from django.urls import path
from .views import show_competition

name = 'partic'

urlpatterns = [
    path('partic/', show_competition),
]