# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-09 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mavi', '0002_auto_20160908_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='guncelYazi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yazi', models.CharField(max_length=1000)),
            ],
        ),
    ]