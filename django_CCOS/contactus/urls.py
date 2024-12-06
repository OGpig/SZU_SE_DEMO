from django.urls import path
from .views import show_contactus

name ='contactus'
urlpatterns = [
    path('contactus/',show_contactus)
]
