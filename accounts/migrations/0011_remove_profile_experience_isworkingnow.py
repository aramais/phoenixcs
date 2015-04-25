# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20150425_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_experience',
            name='isworkingnow',
        ),
    ]
