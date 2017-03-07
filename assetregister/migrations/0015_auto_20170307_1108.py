# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-03-07 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetregister', '0014_asset_emergency_response_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='calibration_frequency',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_serial_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
