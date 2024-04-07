# Generated by Django 5.0.1 on 2024-04-07 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_completed',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
