# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preseed', '0006_auto_20171111_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preseedinstance',
            name='user_ssh_key',
            field=models.TextField(default=''),
        ),
    ]