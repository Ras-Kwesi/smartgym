# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-08 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_auto_20181108_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='From',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='entry',
            name='To',
            field=models.DateTimeField(),
        ),
    ]