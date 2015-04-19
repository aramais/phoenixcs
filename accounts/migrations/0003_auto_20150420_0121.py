# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150417_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('award', models.CharField(max_length=200)),
                ('profile', models.ForeignKey(to='accounts.MyProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile_Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=200)),
                ('jobstart', models.DateField()),
                ('jobend', models.DateField()),
                ('jobdescription', models.TextField()),
                ('profile', models.ForeignKey(to='accounts.MyProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project_Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project', models.CharField(max_length=200)),
                ('projectstart', models.DateField()),
                ('projectend', models.DateField()),
                ('projectdescription', models.TextField()),
                ('profile', models.ForeignKey(to='accounts.MyProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='myprofile',
            name='favourite_snack',
        ),
    ]
