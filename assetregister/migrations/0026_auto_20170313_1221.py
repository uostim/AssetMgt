# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-03-13 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetregister', '0025_auto_20170310_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibrationassetnotificaton',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='environmentalaspectassetnoficiation',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='highvalueassetnotification',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
    ]
