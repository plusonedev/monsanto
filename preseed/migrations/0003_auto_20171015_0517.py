# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preseed', '0002_auto_20171015_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preseedinstance',
            name='instance_id',
            field=models.CharField(editable=False, max_length=100),
        ),
    ]
