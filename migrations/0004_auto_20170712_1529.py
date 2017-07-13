# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RemindMe', '0003_auto_20170706_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='catdesc_text',
            field=models.CharField(help_text=b'Use puns liberally', max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='remdesc_text',
            field=models.TextField(help_text=b'Use puns liberally', max_length=200, null=True, blank=True),
        ),
    ]
