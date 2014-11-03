# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0002_auto_20141103_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenderuser',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 3, 13, 25, 28, 959552, tzinfo=utc), verbose_name=b'registratiedatum', auto_now_add=True),
            preserve_default=False,
        ),
    ]
