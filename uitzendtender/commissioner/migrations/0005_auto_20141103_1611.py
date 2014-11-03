# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commissioner', '0004_auto_20141103_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='branche',
            field=models.ManyToManyField(to='tender.Branch'),
            preserve_default=True,
        ),
    ]
