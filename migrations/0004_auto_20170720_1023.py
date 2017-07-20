# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RemindMe', '0003_auto_20170719_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Created on'),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='rem_date',
            field=models.DateField(verbose_name=b'Reminder date'),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='remdesc_text',
            field=models.TextField(help_text=b'Use puns liberally', max_length=200, null=True, verbose_name=b'Description', blank=True),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='remtitle_text',
            field=models.CharField(max_length=200, verbose_name=b'Title'),
        ),
    ]
