# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RemindMe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='delete_bool',
            new_name='delete_cat',
        ),
        migrations.AddField(
            model_name='reminder',
            name='delete_rem',
            field=models.BooleanField(default=0),
        ),
    ]