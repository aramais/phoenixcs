# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20150425_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_experience',
            name='position',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb7\xd0\xb8\xd1\x86\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project_experience',
            name='position',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb7\xd0\xb8\xd1\x86\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
    ]
