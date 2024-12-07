# Generated by Django 5.1.3 on 2024-12-07 07:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False, verbose_name='地址编号')),
                ('district', models.CharField(max_length=20, verbose_name='校区')),
                ('building', models.CharField(max_length=20, verbose_name='校内建筑')),
                ('room', models.CharField(max_length=20, verbose_name='门牌号')),
            ],
            options={
                'verbose_name': '地址信息',
                'verbose_name_plural': '地址信息',
                'db_table': 'address',
                'ordering': ['-address_id'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False, verbose_name='顾客编号')),
                ('customer_name', models.CharField(max_length=20, verbose_name='顾客昵称')),
                ('customer_password', models.CharField(max_length=20, verbose_name='顾客密码')),
                ('customer_tel', models.CharField(max_length=11, verbose_name='顾客电话')),
                ('customer_status', models.IntegerField(choices=[(0, '离线'), (1, '在线')], default=0, verbose_name='顾客状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.address', verbose_name='地址')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'customer',
                'ordering': ['customer_id'],
            },
        ),
    ]
