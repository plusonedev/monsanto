# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PreseedInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_id', models.CharField(max_length=100)),
                ('version', models.CharField(choices=[('stretch', 'STRETCH')], default='stretch', max_length=12)),
                ('network_type', models.CharField(choices=[('dhcp', 'DHCP'), ('static', 'STATIC')], default='dhcp', max_length=6)),
                ('ip_address', models.CharField(max_length=15)),
                ('mask', models.CharField(max_length=15)),
                ('gateway', models.CharField(max_length=15)),
                ('nameserver', models.CharField(max_length=100)),
                ('hostname', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100)),
                ('ntp_server', models.CharField(max_length=100)),
            ],
        ),
    ]