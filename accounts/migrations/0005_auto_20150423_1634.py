# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20150423_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awards',
            name='profile',
            field=models.ForeignKey(default=1, to='accounts.MyProfile'),
            preserve_default=False,
        ),
    ]
