# Generated by Django 5.1.3 on 2024-12-07 07:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('canteen', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('dish_id', models.AutoField(primary_key=True, serialize=False, verbose_name='商品编号')),
                ('dish_name', models.CharField(max_length=20, verbose_name='商品名称')),
                ('dish_detail', models.CharField(blank=True, max_length=200, null=True, verbose_name='商品描述')),
                ('dish_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='商品价格')),
                ('dish_photo', models.ImageField(blank=True, null=True, upload_to='images/dish', verbose_name='商品照片')),
                ('dish_active', models.IntegerField(choices=[(1, '销售中'), (0, '售罄')], verbose_name='商品状态')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canteen.shop', verbose_name='窗口')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
                'db_table': 'dish',
                'ordering': ['dish_id'],
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False, verbose_name='订单编号')),
                ('order_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='订单价格')),
                ('order_status', models.IntegerField(choices=[(0, '已下单'), (1, '已发货'), (2, '已送达'), (3, '已评价')], default=0, verbose_name='订单状态')),
                ('order_time', models.DateTimeField(auto_now_add=True, verbose_name='下单时间')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='顾客')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dish.dish', verbose_name='商品')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
                'db_table': 'orders',
                'ordering': ['-order_time'],
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False, verbose_name='评价编号')),
                ('comment_score', models.SmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5, verbose_name='评分')),
                ('comment_detail', models.CharField(blank=True, max_length=200, null=True, verbose_name='评价内容')),
                ('comment_time', models.DateTimeField(auto_now_add=True, verbose_name='评价时间')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dish.orders', verbose_name='订单编号')),
            ],
            options={
                'verbose_name': '评价信息',
                'verbose_name_plural': '评价信息',
                'db_table': 'comments',
                'ordering': ['-comment_time'],
            },
        ),
    ]
