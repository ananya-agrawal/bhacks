# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-03-09 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20190309_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='typeofuser',
            field=models.CharField(choices=[('student', 'STUDENT'), ('mentor', 'MENTOR')], default='student', max_length=7),
        ),
    ]
