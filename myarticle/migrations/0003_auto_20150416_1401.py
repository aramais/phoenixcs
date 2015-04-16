# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0002_defaulttag_tagedge'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultarticle',
            name='image',
            field=models.ImageField(default='http://dev.phoenixcs.ru/materials/pp_small.svg', upload_to=b'articlecovers'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='defaultarticle',
            name='text',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='defaultarticle',
            name='url',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='defaulttag',
            name='text',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
    ]
