# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valentine', '0003_userentry_user_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrychoice',
            name='choice_fb',
        ),
    ]
