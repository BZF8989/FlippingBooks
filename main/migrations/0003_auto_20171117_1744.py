# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171117_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='SchoolID',
            field=models.ForeignKey(db_column='SchoolID', on_delete=django.db.models.deletion.CASCADE, to='main.School'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='BookCondition',
            field=models.CharField(choices=[('New', 'New'), ('Poor', 'Poor'), ('Used', 'Used')], max_length=40),
        ),
    ]