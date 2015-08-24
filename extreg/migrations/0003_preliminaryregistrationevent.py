# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extreg', '0002_auto_20150824_0244'),
    ]

    operations = [
        migrations.CreateModel(
            name='preliminaryRegistrationEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('surname', models.CharField(max_length=200, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('name', models.CharField(max_length=200, verbose_name='\u0438\u043c\u044f')),
                ('thirdname', models.CharField(max_length=200, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('email', models.CharField(max_length=200, verbose_name='\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430')),
                ('phone', models.CharField(max_length=200, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('university', models.CharField(max_length=200, verbose_name='\u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442')),
                ('faculty', models.CharField(max_length=200, null=True, verbose_name='\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442')),
                ('course', models.CharField(max_length=200, null=True, verbose_name='\u041a\u0443\u0440\u0441')),
                ('dateEntry', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
