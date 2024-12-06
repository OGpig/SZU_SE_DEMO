# Generated by Django 5.1.3 on 2024-12-07 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surf_competition', '0002_rename_competition_time_competition_competition_begintime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='competition_begintime',
            field=models.DateField(blank=True, null=True, verbose_name='比赛开始时间'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='competition_endtime',
            field=models.DateField(blank=True, null=True, verbose_name='比赛结束时间'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='competition_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='比赛编号'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='competition_info',
            field=models.TextField(blank=True, null=True, verbose_name='比赛简介'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='competition_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='比赛名称'),
        ),
    ]
