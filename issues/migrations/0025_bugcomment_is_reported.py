# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-14 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0024_auto_20181107_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugcomment',
            name='is_reported',
            field=models.BooleanField(default=False),
        ),
    ]
