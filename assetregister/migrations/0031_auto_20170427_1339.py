# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-27 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetregister', '0030_auto_20170413_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_model',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='funded_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='purchase_order_ref',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
