# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0004_auto_20150416_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultarticle',
            name='image',
            field=models.ImageField(upload_to=b'phoenixcs/static/images/articlecovers'),
            preserve_default=True,
        ),
    ]
