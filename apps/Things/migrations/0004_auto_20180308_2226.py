# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-08 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Things', '0003_auto_20180308_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='tech_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='\u6280\u672fID'),
        ),
    ]