from . import views
from django.urls import re_path as url
from django.urls import path
from .views import information, updateInfo

app_name = 'personal_center'
urlpatterns = [
    # path('login/', login),
    # path('register/', register),
    # path('logout/', logout),
    # path('show_info/', show_info, name='show_info'),
    path('info/', information, name='info'),
    path('info/update/', updateInfo, name='update_info'),
]