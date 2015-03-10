# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valentine', '0004_remove_entrychoice_choice_fb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userentry',
            name='place',
        ),
    ]
