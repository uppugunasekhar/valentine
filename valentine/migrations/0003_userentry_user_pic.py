# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valentine', '0002_auto_20150210_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='userentry',
            name='user_pic',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
