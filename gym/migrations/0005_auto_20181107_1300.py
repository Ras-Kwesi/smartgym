# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_auto_20181107_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='info',
            field=models.CharField(max_length=600),
        ),
    ]
