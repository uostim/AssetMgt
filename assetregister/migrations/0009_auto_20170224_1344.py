# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-02-24 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetregister', '0008_remove_asset_calibration_records'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='related_to_other_asset',
        ),
        migrations.AddField(
            model_name='asset',
            name='related_to_other_asset',
            field=models.ManyToManyField(blank=True, null=True, related_name='_asset_related_to_other_asset_+', to='assetregister.Asset'),
        ),
    ]