# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComplexTimeSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=5)),
                ('parameter', models.CharField(max_length=5)),
                ('units', models.CharField(blank=True, max_length=5, null=True)),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=10)),
                ('value', models.FloatField()),
                ('flag', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MultiTimeSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=5)),
                ('date', models.DateField()),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('value', models.FloatField()),
            ],
        ),
    ]