# Generated by Django 5.1.3 on 2024-12-07 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surf_competition', '0004_competition_competition_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='competition_brand',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='比赛品牌'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='competition_category',
            field=models.CharField(blank=True, choices=[('泰迪杯挑战赛', '泰迪杯挑战赛'), ('泰迪杯技能赛', '泰迪杯技能赛'), ('湾区金融数模', '湾区金融数模'), ('华中杯', '华中杯'), ('技能兴鲁', '技能兴鲁'), ('大学生科技节', '大学生科技节')], max_length=30, null=True, verbose_name='比赛类别'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='competition_organization',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='比赛组织者'),
        ),
    ]
