# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-29 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171128_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hunter',
            name='Agility',
            field=models.IntegerField(default=16),
        ),
        migrations.AlterField(
            model_name='hunter',
            name='Intellect',
            field=models.IntegerField(default=93),
        ),
        migrations.AlterField(
            model_name='hunter',
            name='Speed',
            field=models.IntegerField(default=76),
        ),
        migrations.AlterField(
            model_name='hunter',
            name='Stamina',
            field=models.IntegerField(default=90),
        ),
        migrations.AlterField(
            model_name='hunter',
            name='Strength',
            field=models.IntegerField(default=68),
        ),
    ]