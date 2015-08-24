# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extreg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preliminaryregistration',
            name='faculty',
            field=models.CharField(max_length=200, null=True, verbose_name='\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442'),
        ),
        migrations.AlterField(
            model_name='preliminaryregistration',
            name='course',
            field=models.CharField(max_length=200, null=True, verbose_name='\u041a\u0443\u0440\u0441'),
        ),
        migrations.AlterField(
            model_name='preliminaryregistration',
            name='dateEntry',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='preliminaryregistration',
            name='email',
            field=models.CharField(max_length=200, verbose_name='\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='preliminaryregistration',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u0438\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='preliminaryregistration',
            name='phone',
            field=models.CharField(max_length=200, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='preliminaryregistration',
            name='surname',
            field=models.CharField(max_length=200, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='preliminaryregistration',
            name='thirdname',
            field=models.CharField(max_length=200, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e'),
        ),
        migrations.AlterField(
            model_name='preliminaryregistration',
            name='university',
            field=models.CharField(max_length=200, verbose_name='\u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442'),
        ),
    ]
