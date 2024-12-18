# Generated by Django 5.1.3 on 2024-12-07 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultationInfo',
            fields=[
                ('contactus_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sponsor_consultation', models.TextField()),
                ('cooperation_consultation', models.TextField()),
                ('competition_problem_consultation', models.TextField()),
                ('volunteer_recruitment_info', models.TextField()),
                ('email', models.CharField(max_length=20, unique=True)),
                ('feedback_form', models.TextField()),
            ],
            options={
                'db_table': 'consultation_info',
            },
        ),
    ]
