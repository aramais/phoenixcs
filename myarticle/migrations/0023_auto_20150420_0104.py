# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0022_auto_20150417_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 20)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default=b'phoenixcs_logo_short.jpg', upload_to=b'images'),
            preserve_default=True,
        ),
    ]
