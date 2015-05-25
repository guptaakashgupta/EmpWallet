# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employeeID', models.CharField(max_length=250)),
                ('balance', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transcation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=500)),
                ('valueOfTranscation', models.IntegerField()),
                ('status', models.CharField(default=b'created', max_length=1)),
                ('employeeID', models.ForeignKey(to='EmployeeManage.Employee')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
