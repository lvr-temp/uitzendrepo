# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0004_auto_20141103_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, verbose_name=b'branchenaam')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default=b'Nederland', max_length=80, verbose_name=b'land')),
                ('code', models.CharField(default=b'NLD', max_length=3, verbose_name=b'ISO drieletterige code')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='tenderuser',
            name='userrole',
            field=models.CharField(default=b'0', max_length=20, choices=[(b'0', b'guest'), (b'1', b'commissioner'), (b'2', b'agency'), (b'3', b'staff')]),
            preserve_default=True,
        ),
    ]
