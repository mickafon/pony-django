# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-18 13:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elder', '0010_auto_20170718_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oldperson',
            name='birthdate',
        ),
        migrations.AddField(
            model_name='oldperson',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(1900, 1, 1, 0, 0), verbose_name='Birthday'),
        ),
    ]
