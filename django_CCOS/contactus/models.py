# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ConsultationInfo(models.Model):
    contactus_id = models.BigAutoField(primary_key=True)
    sponsor_consultation = models.TextField()
    cooperation_consultation = models.TextField()
    competition_problem_consultation = models.TextField()
    volunteer_recruitment_info = models.TextField()
    email = models.CharField(unique=True, max_length=20)
    feedback_form = models.TextField()

    class Meta:
        db_table = 'consultation_info'
    
    def __str__(self):
        return str(self.contactus_id)
