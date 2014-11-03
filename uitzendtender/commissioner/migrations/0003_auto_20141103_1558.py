# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commissioner', '0002_auto_20141103_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='branche',
            field=models.ManyToManyField(to='tender.Branch', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(null=True, verbose_name=b'omschrijving bedrijf', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.URLField(max_length=100, null=True, verbose_name=b'website', blank=True),
            preserve_default=True,
        ),
    ]
