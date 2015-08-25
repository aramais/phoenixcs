# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extreg', '0004_auto_20150824_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preliminaryregistration',
            name='course',
        ),
        migrations.AddField(
            model_name='preliminaryregistration',
            name='studyForm',
            field=models.CharField(default=b'bach', max_length=200, null=True, verbose_name='\u0421\u0442\u0435\u043f\u0435\u043d\u044c', choices=[(b'bach', b'\xd0\x91\xd0\xb0\xd0\xba\xd0\xb0\xd0\xbb\xd0\xb0\xd0\xb2\xd1\x80\xd0\xb8\xd0\xb0\xd1\x82'), (b'spec', b'\xd0\xa1\xd0\xbf\xd0\xb5\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x82\xd0\xb5\xd1\x82'), (b'mag', b'\xd0\x9c\xd0\xb0\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x82\xd1\x83\xd1\x80\xd0\xb0'), (b'other', b'\xd0\x98\xd0\xbd\xd0\xbe\xd0\xb5')]),
        ),
        migrations.AddField(
            model_name='preliminaryregistration',
            name='yearEnd',
            field=models.CharField(default=b'2017', max_length=200, null=True, verbose_name='\u0413\u043e\u0434 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f', choices=[(b'2000', b'2000'), (b'2001', b'2001'), (b'2002', b'2002'), (b'2003', b'2003'), (b'2004', b'2004'), (b'2005', b'2005'), (b'2006', b'2006'), (b'2007', b'2007'), (b'2008', b'2008'), (b'2009', b'2009'), (b'2010', b'2010'), (b'2011', b'2011'), (b'2012', b'2012'), (b'2013', b'2013'), (b'2014', b'2014'), (b'2015', b'2015'), (b'2016', b'2016'), (b'2017', b'2017'), (b'2018', b'2018'), (b'2019', b'2019'), (b'2020', b'2020'), (b'2021', b'2021'), (b'2022', b'2022'), (b'2023', b'2023'), (b'2024', b'2024'), (b'other', b'\xd0\x94\xd1\x80\xd1\x83\xd0\xb3\xd0\xbe\xd0\xb5')]),
        ),
    ]
