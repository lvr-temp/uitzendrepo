# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commissioner', '0003_auto_20141103_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.CharField(default=b'U', max_length=3, verbose_name=b'geslacht', choices=[(b'M', b'man'), (b'F', b'vrouw'), (b'U', b'onbekend')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='prefix',
            field=models.CharField(max_length=40, null=True, verbose_name=b'voorvoegsel', blank=True),
            preserve_default=True,
        ),
    ]
