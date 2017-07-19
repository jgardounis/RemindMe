# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RemindMe', '0011_auto_20170713_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='catname_text',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
