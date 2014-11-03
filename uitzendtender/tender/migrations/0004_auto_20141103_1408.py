# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0003_tenderuser_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenderuser',
            name='userrole',
            field=models.CharField(default=0, max_length=20, choices=[(0, b'guest'), (1, b'commissioner'), (2, b'agency'), (3, b'staff')]),
            preserve_default=True,
        ),
    ]
