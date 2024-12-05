from django.contrib import admin

# Register your models here.
from .models import Surf,Inquiry,Competition

admin.site.register(Surf)
admin.site.register(Inquiry)
admin.site.register(Competition)