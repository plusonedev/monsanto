# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preseed', '0004_auto_20171019_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='preseedinstance',
            name='apps',
            field=models.TextField(default=''),
        ),
    ]
