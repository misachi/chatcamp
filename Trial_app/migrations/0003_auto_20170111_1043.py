# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-11 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trial_app', '0002_auto_20170111_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Creates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trial_app.Registration')),
            ],
        ),
        migrations.CreateModel(
            name='Feeds',
            fields=[
                ('feeds_id', models.AutoField(primary_key=True, serialize=False)),
                ('feeds', models.CharField(max_length=200)),
                ('time_posted', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('friends_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('notifications', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_posted', models.TimeField()),
                ('app_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trial_app.Registration')),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trial_app.Comments')),
                ('feeds_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trial_app.Feeds')),
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
            name='ShootsMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_sent', models.TimeField()),
                ('app_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trial_app.Registration')),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trial_app.Messages')),
            ],
        ),
        migrations.AddField(
            model_name='creates',
            name='profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trial_app.Profile'),
        ),
    ]
