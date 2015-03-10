# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valentine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentry',
            name='friends_count',
            field=models.IntegerField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
    ]
