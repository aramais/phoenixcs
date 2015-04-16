# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0003_auto_20150416_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultarticle',
            name='image',
            field=models.ImageField(upload_to=b'images/articlecovers'),
            preserve_default=True,
        ),
    ]
