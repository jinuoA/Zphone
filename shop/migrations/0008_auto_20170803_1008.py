# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-08-03 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20170803_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taggoods',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, max_length=2, verbose_name='\u6298\u6263'),
        ),
    ]