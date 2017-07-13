# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RemindMe', '0010_auto_20170713_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='catdesc_text',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
    ]
