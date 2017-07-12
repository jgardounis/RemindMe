# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RemindMe', '0002_auto_20170629_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='rem_date',
            field=models.DateField(verbose_name=b'reminder date'),
        ),
    ]
