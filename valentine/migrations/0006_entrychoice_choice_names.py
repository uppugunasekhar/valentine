# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('valentine', '0005_remove_userentry_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrychoice',
            name='choice_names',
            field=models.CharField(default=datetime.datetime(2015, 2, 16, 9, 39, 22, 154854, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
