from django.contrib import admin

# Register your models here.
from .models import Contactus,Consult,Feedbackform,Volunteerrecruitment

admin.site.register(Contactus)
admin.site.register(Consult)
admin.site.register(Feedbackform)
admin.site.register(Volunteerrecruitment)