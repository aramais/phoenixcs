# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150420_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awards',
            name='profile',
            field=models.ForeignKey(blank=True, to='accounts.MyProfile', null=True),
            preserve_default=True,
        ),
    ]
