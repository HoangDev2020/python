# Generated by Django 3.1.7 on 2021-04-22 06:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 22, 2, 59, 24, 65071)),
        ),
    ]
