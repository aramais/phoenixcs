# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagEdge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article', models.ForeignKey(to='myarticle.DefaultArticle')),
                ('tag', models.ForeignKey(to='myarticle.DefaultTag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
