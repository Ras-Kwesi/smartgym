# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-03 19:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='users',
            field=models.ManyToManyField(related_name='chatroom', to=settings.AUTH_USER_MODEL),
        ),
    ]
