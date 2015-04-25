# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20150423_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_experience',
            name='isworkingnow',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9f\xd0\xbe \xd1\x81\xd0\xb5\xd0\xb9 \xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='awards',
            name='award',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb3\xd1\x80\xd0\xb0\xd0\xb4\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile_experience',
            name='company',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile_experience',
            name='jobdescription',
            field=models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile_experience',
            name='jobend',
            field=models.DateField(verbose_name=b'\xd0\x9e\xd0\xba\xd0\xbe\xd0\xbd\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile_experience',
            name='jobstart',
            field=models.DateField(verbose_name=b'\xd0\x9d\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xbe \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project_experience',
            name='project',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project_experience',
            name='projectdescription',
            field=models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x80\xd0\xbe\xd0\xbb\xd0\xb8 \xd0\xb2 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82\xd0\xb5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project_experience',
            name='projectend',
            field=models.DateField(verbose_name=b'\xd0\x9e\xd0\xba\xd0\xbe\xd0\xbd\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project_experience',
            name='projectstart',
            field=models.DateField(verbose_name=b'\xd0\x9d\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xbe \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82\xd0\xb0'),
            preserve_default=True,
        ),
    ]
