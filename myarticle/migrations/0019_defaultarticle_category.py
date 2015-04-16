# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0018_auto_20150416_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultarticle',
            name='category',
            field=models.ForeignKey(default=0, to='myarticle.Category'),
            preserve_default=True,
        ),
    ]
