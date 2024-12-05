# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from customer.models import Customer

class Surf(models.Model):
    surf_id = models.IntegerField(primary_key=True,verbose_name='浏览编号')
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    competition = models.ForeignKey('Competition', models.DO_NOTHING, blank=True, null=True)
    surf_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surf'
        verbose_name = '浏览'
        verbose_name_plural = '浏览'

    def __str__(self):
        return str(self.surf_id)


class Competition(models.Model):
    competition_id = models.IntegerField(primary_key=True)
    competition_name = models.CharField(max_length=20, blank=True, null=True)
    competition_info = models.TextField(blank=True, null=True)
    competition_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'competition'
        verbose_name = '竞赛'
        verbose_name_plural = '竞赛'

    def __str__(self):
        return str(self.competition_id)


class Inquiry(models.Model):
    iqui = models.IntegerField(primary_key=True)
    inquiry_time = models.DateTimeField(blank=True, null=True)
    inquiry_result = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inquiry'
        verbose_name = '浏览'
        verbose_name_plural = '浏览'

    def __str__(self):
        return str(self.iqui)

