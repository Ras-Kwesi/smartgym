# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-08 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_auto_20181108_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='picture/'),
        ),
    ]