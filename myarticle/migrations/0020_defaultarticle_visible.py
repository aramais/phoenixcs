# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0019_defaultarticle_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultarticle',
            name='visible',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
