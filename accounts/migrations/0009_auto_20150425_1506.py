# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20150425_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_experience',
            name='isworkingnow',
            field=models.BooleanField(default=True, verbose_name=b'\xd0\x9f\xd0\xbe \xd1\x81\xd0\xb5\xd0\xb9 \xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c'),
            preserve_default=True,
        ),
    ]
