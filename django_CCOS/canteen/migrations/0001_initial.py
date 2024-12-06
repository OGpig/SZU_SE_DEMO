# Generated by Django 5.1.3 on 2024-12-06 03:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canteen',
            fields=[
                ('canteen_id', models.AutoField(primary_key=True, serialize=False, verbose_name='分区编号')),
                ('canteen_name', models.CharField(max_length=10, verbose_name='分区名称')),
                ('canteen_photo', models.ImageField(blank=True, null=True, upload_to='images/canteen', verbose_name='分区照片')),
                ('sanitation_level', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1, verbose_name='卫生等级')),
                ('canteen_active', models.CharField(choices=[('营业中', '营业中'), ('歇业中', '歇业中')], max_length=10, verbose_name='分区状态')),
            ],
            options={
                'verbose_name': '分区信息',
                'verbose_name_plural': '分区信息',
                'db_table': 'canteen',
                'ordering': ['canteen_id'],
            },
        ),
        migrations.CreateModel(
            name='ShopManager',
            fields=[
                ('manager_id', models.AutoField(primary_key=True, serialize=False, verbose_name='经营者编号')),
                ('manager_name', models.CharField(max_length=20, verbose_name='经营者昵称')),
                ('manager_password', models.CharField(max_length=20, verbose_name='经营者密码')),
                ('manager_tel', models.CharField(max_length=11, verbose_name='经营者电话')),
                ('manager_status', models.IntegerField(choices=[(0, '离线'), (1, '在线')], default=0, verbose_name='经营者状态')),
                ('manage_shop_num', models.IntegerField(verbose_name='经营店铺数')),
            ],
            options={
                'verbose_name': '店铺经营者信息',
                'verbose_name_plural': '店铺经营者信息',
                'db_table': 'shop_manager',
                'ordering': ['manager_id'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.AutoField(primary_key=True, serialize=False, verbose_name='店铺编号')),
                ('shop_name', models.CharField(max_length=20, verbose_name='店铺名称')),
                ('shop_detail', models.CharField(blank=True, max_length=200, null=True, verbose_name='店铺描述')),
                ('shop_photo', models.ImageField(blank=True, null=True, upload_to='images/shop', verbose_name='店铺照片')),
                ('shop_active', models.IntegerField(choices=[(1, '营业中'), (0, '歇业中')], verbose_name='店铺状态')),
                ('canteen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canteen.canteen', verbose_name='分区')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='canteen.shopmanager', verbose_name='店铺经营者')),
            ],
            options={
                'verbose_name': '店铺信息',
                'verbose_name_plural': '店铺信息',
                'db_table': 'shop',
                'ordering': ['shop_id'],
            },
        ),
    ]
