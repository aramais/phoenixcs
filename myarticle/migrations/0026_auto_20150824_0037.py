# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0025_auto_20150423_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(default=datetime.date(2015, 8, 24)),
        ),
    ]
