# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0020_defaultarticle_visible'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('url', models.SlugField(unique=True)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to=b'images')),
                ('date', models.DateField(default=datetime.date(2015, 4, 16))),
                ('author', models.CharField(default=b'author unknown', max_length=200)),
                ('visible', models.BooleanField(default=False)),
                ('category', models.ForeignKey(default=0, to='myarticle.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='DefaultTag',
            new_name='Tag',
        ),
        migrations.RemoveField(
            model_name='defaultarticle',
            name='category',
        ),
        migrations.AlterField(
            model_name='tagedge',
            name='article',
            field=models.ForeignKey(to='myarticle.Article'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='DefaultArticle',
        ),
    ]
