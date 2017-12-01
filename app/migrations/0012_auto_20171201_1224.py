# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-01 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_merge_20171130_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='new_mammoths',
        ),
        migrations.AlterField(
            model_name='hunt',
            name='circumstances',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='hunter',
            name='Agility',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hunter',
            name='Intellect',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hunter',
            name='Speed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hunter',
            name='Stamina',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hunter',
            name='Strength',
            field=models.IntegerField(default=0),
        ),
    ]
