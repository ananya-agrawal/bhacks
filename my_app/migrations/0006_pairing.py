# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-03-09 06:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0005_user_info_type_of_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pairing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(default=0)),
                ('Ack1', models.BooleanField(default=False)),
                ('Ack2', models.BooleanField(default=False)),
                ('Ack3', models.BooleanField(default=False)),
                ('Ack4', models.BooleanField(default=False)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Post')),
            ],
        ),
    ]
