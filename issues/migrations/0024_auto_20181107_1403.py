# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-07 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0023_auto_20181107_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='status',
            field=models.CharField(choices=[('Pending Payment', 'Pending Payment'), ('Open', 'Open'), ('Target not Reached', 'Target not Reached'), ('Under Review', 'Under Review'), ('Under Development', 'Under Development'), ('Testing', 'Testing'), ('Deployed', 'Deployed')], default='Pending Payment', max_length=20),
        ),
    ]
