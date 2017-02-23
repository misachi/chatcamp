# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-23 11:05
from __future__ import unicode_literals

from django.db import migrations, models
import user_profile.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20170216_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=user_profile.models.upload_location, width_field='width_field'),
        ),
    ]
