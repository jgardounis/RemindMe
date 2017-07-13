# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RemindMe', '0004_auto_20170712_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='catdesc_text',
            field=models.TextField(help_text=b'Use puns liberally', max_length=200, null=True, blank=True),
        ),
    ]
