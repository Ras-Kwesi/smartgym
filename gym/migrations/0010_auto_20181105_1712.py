# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 14:12
from __future__ import unicode_literals

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0009_auto_20181105_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='location',
            field=geoposition.fields.GeopositionField(max_length=42),
        ),
    ]
