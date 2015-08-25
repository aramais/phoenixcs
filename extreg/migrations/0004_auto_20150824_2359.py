# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extreg', '0003_preliminaryregistrationevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preliminaryregistration',
            name='dateEntry',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='preliminaryregistration',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='preliminaryregistrationevent',
            name='dateEntry',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='preliminaryregistrationevent',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430'),
        ),
    ]
