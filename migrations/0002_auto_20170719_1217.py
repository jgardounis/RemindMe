# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RemindMe', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category'},
        ),
        migrations.AlterField(
            model_name='category',
            name='catdesc_text',
            field=models.TextField(max_length=200, null=True, verbose_name=b'Description', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='catname_text',
            field=models.CharField(max_length=200, verbose_name=b'Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Created on'),
        ),
    ]
