# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0017_auto_20150416_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultarticle',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 16)),
            preserve_default=True,
        ),
    ]
