# Generated by Django 5.1.3 on 2024-12-07 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surf_competition', '0003_alter_competition_competition_begintime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='competition_brand',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='competition_category',
            field=models.CharField(blank=True, choices=[('泰迪杯挑战赛', '泰迪杯挑战赛'), ('泰迪杯技能赛', '泰迪杯技能赛'), ('湾区金融数模', '湾区金融数模'), ('华中杯', '华中杯'), ('技能兴鲁', '技能兴鲁'), ('大学生科技节', '大学生科技节')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='competition_organization',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='competition_teams',
            field=models.IntegerField(blank=True, null=True, verbose_name='比赛队伍数'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='competition_status',
            field=models.CharField(blank=True, choices=[('未开始', '未开始'), ('进行中', '进行中'), ('已结束', '已结束')], max_length=40, null=True, verbose_name='比赛状态'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='competition_type',
            field=models.CharField(blank=True, choices=[('数据挖掘', '数据挖掘'), ('数据分析', '数据分析'), ('数学建模', '数学建模'), ('金融数学', '金融数学'), ('人工智能', '人工智能'), ('大数据应用', '大数据应用')], max_length=40, null=True, verbose_name='比赛类型'),
        ),
    ]