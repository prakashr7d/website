# Generated by Django 3.0.3 on 2020-09-20 18:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 20, 18, 57, 22, 293194, tzinfo=utc)),
        ),
    ]
