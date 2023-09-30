# Generated by Django 4.2.2 on 2023-09-30 08:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_leaverequest_leave_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequest',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
