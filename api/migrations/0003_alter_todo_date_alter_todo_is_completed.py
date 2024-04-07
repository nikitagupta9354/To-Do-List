# Generated by Django 5.0.1 on 2024-04-07 09:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_todo_date_alter_todo_is_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_completed',
            field=models.CharField(default='Pending', max_length=10),
        ),
    ]