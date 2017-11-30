# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-30 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20171130_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hunt',
            name='pits',
        ),
        migrations.AddField(
            model_name='hunt',
            name='pit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Pit'),
        ),
    ]