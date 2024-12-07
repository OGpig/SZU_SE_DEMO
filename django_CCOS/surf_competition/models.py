# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.text import slugify
from django.shortcuts import redirect
from customer.models import Customer

class Surf(models.Model):
    surf_id = models.IntegerField(primary_key=True,verbose_name='浏览编号')
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    competition = models.ForeignKey('Competition', models.DO_NOTHING, blank=True, null=True)
    surf_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'surf'
        verbose_name = '浏览'
        verbose_name_plural = '浏览'

    def __str__(self):
        return str(self.surf_id)


class Competition(models.Model):
    COMPETITION_STATUS_CHOICES = [
        ('未开始', '未开始'),
        ('进行中', '进行中'),
        ('已结束', '已结束'),
    ]

    COMPETITION_TYPE_CHOICES = [
        ('数据挖掘', '数据挖掘'),
        ('数据分析', '数据分析'),
        ('数学建模', '数学建模'),
        ('金融数学', '金融数学'),
        ('人工智能', '人工智能'),
        ('大数据应用', '大数据应用'),
    ]
    competition_id = models.IntegerField(primary_key=True,verbose_name='比赛编号')
    competition_name = models.CharField(max_length=20, blank=True, null=True,verbose_name='比赛名称')
    competition_info = models.TextField(blank=True, null=True,verbose_name='比赛简介')
    competition_begintime = models.DateField(blank=True, null=True,verbose_name='比赛开始时间')
    competition_endtime = models.DateField(blank=True, null=True,verbose_name='比赛结束时间')
    competition_teams = models.IntegerField(blank=True, null=True,verbose_name='比赛队伍数')
    competition_prize = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='比赛奖金')
    competition_type = models.CharField(
        max_length=40, 
        choices=COMPETITION_TYPE_CHOICES, 
        blank=True, 
        null=True, 
        verbose_name='比赛类型'
    )
    competition_status = models.CharField(
        max_length=40, 
        choices=COMPETITION_STATUS_CHOICES, 
        blank=True, 
        null=True, 
        verbose_name='比赛状态'
    )
    competition_category = models.CharField(
        max_length=30,
        choices=[
            ('泰迪杯挑战赛', '泰迪杯挑战赛'),
            ('泰迪杯技能赛', '泰迪杯技能赛'),
            ('湾区金融数模', '湾区金融数模'),
            ('华中杯', '华中杯'),
            ('技能兴鲁', '技能兴鲁'),
            ('大学生科技节', '大学生科技节'),
        ],
        blank=True,
        null=True,
        verbose_name='比赛类别'
    )
    competition_brand = models.CharField(max_length=50, blank=True, null=True,verbose_name='比赛品牌')  # 比赛品牌
    competition_organization = models.CharField(max_length=100, blank=True, null=True,verbose_name='比赛组织者')  # 比赛组织单位

    class Meta:
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
        db_table = 'inquiry'
        verbose_name = '浏览'
        verbose_name_plural = '浏览'

    def __str__(self):
        return str(self.iqui)

