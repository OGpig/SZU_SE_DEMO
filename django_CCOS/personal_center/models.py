# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_avatar = models.CharField(max_length=255, blank=True, null=True)
    user_role = models.CharField(max_length=255, blank=True, null=True)
    user_sex = models.CharField(max_length=255, blank=True, null=True)
    user_describe = models.CharField(max_length=255, blank=True, null=True)
    user_birthday = models.CharField(max_length=255, blank=True, null=True)
    user_school = models.CharField(max_length=255, blank=True, null=True)
    user_phone = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_wechat = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
