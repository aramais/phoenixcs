# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0023_auto_20150420_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default=b'images/default.jpg', upload_to=b'images'),
            preserve_default=True,
        ),
    ]
