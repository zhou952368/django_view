# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-11-16 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo04', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Girl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('published', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=20, null=True)),
                ('type', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=255)),
                ('used', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'girls',
            },
        ),
    ]
