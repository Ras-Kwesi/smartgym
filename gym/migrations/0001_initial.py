# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 09:20
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_pic', models.ImageField(blank=True, upload_to='images/')),
                ('user_type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Client'), (2, 'Trainer'), (3, 'Gym manager')], null=True)),
                ('contact', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('info', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('description', models.TextField(max_length=100)),
                ('event_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('working_hours', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GymManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=100)),
                ('profilepic', models.ImageField(blank=True, upload_to='picture/')),
            ],
        ),
        migrations.CreateModel(
            name='Gymnast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(max_length=10)),
                ('height', models.CharField(max_length=10)),
                ('goal', models.CharField(choices=[('Losing weight', 'Losing weight'), ('Getting toned', 'Getting toned'), ('Getting bigger', 'Getting bigger'), ('Maintain fitness', 'Maintain fitness')], max_length=30)),
                ('contact', models.CharField(blank=True, max_length=30)),
                ('bio', models.TextField(max_length=50)),
                ('chatroom', models.ManyToManyField(to='gym.Chat')),
                ('gym', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Gym')),
            ],
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.Gym')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('post', models.TextField(max_length=100)),
                ('chatroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='gym.Chat')),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=30)),
                ('specially', models.CharField(max_length=30)),
                ('year_Experience', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='join',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gymnast',
            name='user',
            field=models.ManyToManyField(related_name='gymnast', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gymmanager',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gym_manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gym',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='administrate', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='gym',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.Gym'),
        ),
    ]
