# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-02-25 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetregister', '0002_auto_20170225_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnviroAspects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aspect', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='environmental_aspects',
            field=models.ManyToManyField(blank=True, to='assetregister.EnviroAspects'),
        ),
    ]