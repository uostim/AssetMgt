# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-03-07 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetregister', '0016_auto_20170307_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='amrc_equipment_id',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
