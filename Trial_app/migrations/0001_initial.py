# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-29 09:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=300)),
                ('time_posted', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('feeds_id', models.AutoField(primary_key=True, serialize=False)),
                ('feeds', models.CharField(max_length=200)),
                ('time_posted', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('friends_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('notifications', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_id', models.AutoField(primary_key=True, serialize=False)),
                ('contacts', models.TextField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('skills', models.CharField(max_length=500)),
                ('profession', models.TextField(max_length=100)),
                ('brief_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('app_user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='app_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trial_app.Registration'),
        ),
        migrations.AddField(
            model_name='friend',
            name='user_friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trial_app.Registration'),
        ),
    ]
