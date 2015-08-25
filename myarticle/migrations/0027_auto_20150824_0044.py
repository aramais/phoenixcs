# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0026_auto_20150824_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
