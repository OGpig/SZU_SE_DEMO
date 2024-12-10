# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Consult(models.Model):
    contactus_id = models.IntegerField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    sponsor_consultation = models.TextField(blank=True, null=True)
    cooperation_consultation = models.TextField(blank=True, null=True)
    competition_consultation = models.TextField(blank=True, null=True)
    
    class Meta:
        
        db_table = 'consult'
        verbose_name = '咨询'
        verbose_name_plural = '咨询'


class Feedbackform(models.Model):
    contactus_id = models.IntegerField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    feedbackinformation = models.TextField(blank=True, null=True)
    
    class Meta:
        
        db_table = 'feedbackform'
        verbose_name = '反馈表单'
        verbose_name_plural = '反馈表单'


class Volunteerrecruitment(models.Model):
    contactus_id = models.IntegerField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    recruitmentrequirements = models.TextField(blank=True, null=True)
        
    class Meta:
       
        db_table = 'volunteerrecruitment'
        verbose_name = '志愿者招募'
        verbose_name_plural = '志愿者招募'


class Contactus(models.Model):
    contactus_id = models.IntegerField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return str(self.contactus_id)
    
    class Meta:
        
        db_table = 'contactus'
        verbose_name = '联系我们'
        verbose_name_plural = '联系我们'
