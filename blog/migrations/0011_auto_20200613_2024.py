# Generated by Django 2.1.11 on 2020-06-13 14:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200613_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 13, 14, 54, 25, 73515, tzinfo=utc)),
        ),
    ]
