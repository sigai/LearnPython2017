# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='code',
            field=models.CharField(default='SA', max_length=32, null=True),
        ),
    ]
