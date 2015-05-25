# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EmployeeManage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalEmployee',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('employeeID', models.CharField(max_length=250)),
                ('balance', models.IntegerField()),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical employee',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalTranscation',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('time', models.DateTimeField(editable=False, blank=True)),
                ('description', models.CharField(max_length=500)),
                ('employeeID_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('valueOfTranscation', models.IntegerField()),
                ('status', models.CharField(default=b'created', max_length=1)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical transcation',
            },
            bases=(models.Model,),
        ),
    ]
