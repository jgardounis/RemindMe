# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catname_text', models.CharField(max_length=200)),
                ('catdesc_text', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(verbose_name=b'date created')),
                ('delete_bool', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remtitle_text', models.CharField(max_length=200)),
                ('remdesc_text', models.CharField(max_length=200)),
                ('rem_date', models.DateTimeField(verbose_name=b'reminder date')),
                ('created_date', models.DateTimeField(verbose_name=b'date created')),
                ('category', models.ForeignKey(to='RemindMe.Category')),
            ],
        ),
    ]
