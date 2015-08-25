# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extreg', '0005_auto_20150825_0013'),
    ]

    operations = [
        migrations.DeleteModel(
            name='preliminaryRegistrationEvent',
        ),
        migrations.AddField(
            model_name='preliminaryregistration',
            name='qualifier',
            field=models.CharField(default=b'main', max_length=20, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb7\xd0\xb0\xd1\x8f\xd0\xb2\xd0\xba\xd0\xb8', choices=[(b'main', b'Selection'), (b'm1', b'Event1'), (b'm2', b'Event2'), (b'm3', b'Event3'), (b'z1', b'online1'), (b'z2', b'online2')]),
        ),
        migrations.AlterField(
            model_name='preliminaryregistration',
            name='studyForm',
            field=models.CharField(default=b'bach', max_length=200, null=True, verbose_name='\u0421\u0442\u0435\u043f\u0435\u043d\u044c', choices=[(b'bach', b'\xd0\x91\xd0\xb0\xd0\xba\xd0\xb0\xd0\xbb\xd0\xb0\xd0\xb2\xd1\x80\xd0\xb8\xd0\xb0\xd1\x82'), (b'spec', b'\xd0\xa1\xd0\xbf\xd0\xb5\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x82\xd0\xb5\xd1\x82'), (b'mag', b'\xd0\x9c\xd0\xb0\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x82\xd1\x83\xd1\x80\xd0\xb0'), (b'other', b'\xd0\x94\xd1\x80\xd1\x83\xd0\xb3\xd0\xbe\xd0\xb5')]),
        ),
        migrations.AlterField(
            model_name='preliminaryregistration',
            name='university',
            field=models.CharField(max_length=200, verbose_name='\u0412\u0423\u0417'),
        ),
    ]
