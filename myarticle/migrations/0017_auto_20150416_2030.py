# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0016_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultarticle',
            name='author',
            field=models.CharField(default=b'author unknown', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='defaultarticle',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 16), auto_now_add=True),
            preserve_default=True,
        ),
    ]
