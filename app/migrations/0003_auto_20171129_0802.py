# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 08:02
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
            field=models.IntegerField(default=52),
        ),
        migrations.AlterField(
            model_name='hunter',
            name='Intellect',
            field=models.IntegerField(default=58),
        ),
        migrations.AlterField(
            model_name='hunter',
            name='Speed',
            field=models.IntegerField(default=97),
        ),
        migrations.AlterField(
            model_name='hunter',
            name='Stamina',
            field=models.IntegerField(default=17),
        ),
        migrations.AlterField(
            model_name='hunter',
            name='Strength',
            field=models.IntegerField(default=68),
        ),
    ]