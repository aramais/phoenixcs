# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0013_auto_20150416_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultarticle',
            name='image',
            field=models.ImageField(upload_to=b'/'),
            preserve_default=True,
        ),
    ]
