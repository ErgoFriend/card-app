# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-18 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardtitle', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('liked', models.IntegerField()),
                ('carddate', models.DateTimeField()),
                ('cardtag', models.TextField()),
                ('cardcaregory', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=256)),
                ('language_color', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('detail', models.TextField()),
                ('tag', models.TextField()),
                ('date', models.DateTimeField()),
                ('category', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_mail', models.TextField()),
                ('password', models.TextField()),
                ('name', models.CharField(max_length=256)),
                ('following', models.IntegerField()),
                ('fllower', models.IntegerField()),
                ('star', models.IntegerField()),
                ('profile_picture', models.FileField(upload_to='./upload/')),
            ],
        ),
    ]
