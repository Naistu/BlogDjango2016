# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-18 13:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160818_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='exp',
        ),
    ]
