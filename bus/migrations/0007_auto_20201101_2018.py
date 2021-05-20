# Generated by Django 3.1 on 2020-11-01 14:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0006_auto_20201101_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 1, 14, 48, 52, 889645, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='passengerdetail',
            name='mobile_number',
            field=models.CharField(max_length=100),
        ),
    ]