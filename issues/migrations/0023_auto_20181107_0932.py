# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-07 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0022_auto_20181106_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='feature',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='feature',
            name='status',
            field=models.CharField(choices=[('Pending Payment', 'Pending Payment'), ('Target not Reached', 'Target not Reached'), ('Open', 'Open'), ('Under Review', 'Under Review'), ('Under Development', 'Under Development'), ('Testing', 'Testing'), ('Deployed', 'Deployed')], default='Pending Payment', max_length=20),
        ),
    ]
