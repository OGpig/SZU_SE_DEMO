"""django_CCOS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path

# 用于 include 其他模板所在的 url
from django.urls import re_path as url
from django.conf.urls import include

# 用于 图片 静态存储
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', include('home_page.urls')),
    
    path('admin/', admin.site.urls),
    path('customer/', include('customer.urls')),

    path('surf_competition/', include('surf_competition.urls')),
    path('contactus/', include('contactus.urls')),
    path('teacher_information/', include('teacher_information.urls')),
    path('', include('partic.urls')),

    path('', include('partic.urls')),
    path('personal_center/', include('personal_center.urls')),
]

# 把 media 路径也添加上
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)