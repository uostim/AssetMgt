# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-03-06 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetregister', '0013_auto_20170306_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='emergency_response_information',
            field=models.TextField(blank=True),
        ),
    ]