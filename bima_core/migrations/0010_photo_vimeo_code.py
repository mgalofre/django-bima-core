# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-27 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bima_core', '0009_auto_20171002_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='vimeo_code',
            field=models.CharField(blank=True, max_length=100, verbose_name='Vimeo code'),
        ),
    ]