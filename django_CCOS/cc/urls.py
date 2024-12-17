from django.urls import path
from .views import show_competitione

name = 'cc'

urlpatterns = [
    path('', show_competitione),
]