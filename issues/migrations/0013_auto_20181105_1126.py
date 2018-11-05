# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0012_bug_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='resolved_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='bug',
            name='status',
            field=models.CharField(choices=[('O', 'Open'), ('R', 'Under Review'), ('T', 'Testing'), ('C', 'Closed')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]