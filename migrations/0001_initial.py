# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catname_text', models.CharField(max_length=200)),
                ('catdesc_text', models.TextField(max_length=200, null=True, blank=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('delete_cat', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remtitle_text', models.CharField(max_length=200)),
                ('remdesc_text', models.TextField(help_text=b'Use puns liberally', max_length=200, null=True, blank=True)),
                ('rem_date', models.DateField(verbose_name=b'reminder date')),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('delete_rem', models.BooleanField(default=0)),
                ('category', models.ForeignKey(to='RemindMe.Category')),
            ],
        ),
    ]
