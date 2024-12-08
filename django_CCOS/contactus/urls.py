from django.urls import path
from .views import show_contactus,submit_contact_form

name ='contactus'
urlpatterns = [
    path('',show_contactus),
    path('submitContactForm/', submit_contact_form,name='submit_contact_form'),
]
