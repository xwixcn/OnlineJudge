# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20151211_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tfa_token',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
