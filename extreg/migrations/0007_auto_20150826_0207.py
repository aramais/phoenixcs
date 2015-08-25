# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extreg', '0006_auto_20150826_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preliminaryregistration',
            name='qualifier',
            field=models.CharField(default=b'default', max_length=20, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb7\xd0\xb0\xd1\x8f\xd0\xb2\xd0\xba\xd0\xb8'),
        ),
    ]
