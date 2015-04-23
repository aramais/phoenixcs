# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0024_auto_20150420_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 23)),
            preserve_default=True,
        ),
    ]
