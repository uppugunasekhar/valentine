# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntryChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_fb', models.EmailField(max_length=100)),
                ('choice_email', models.EmailField(max_length=100)),
                ('choice_altemail', models.EmailField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match_email', models.EmailField(max_length=100, null=True, blank=True)),
                ('user_fullname', models.CharField(max_length=100)),
                ('user_email', models.EmailField(unique=True, max_length=100)),
                ('date_of_selection', models.DateTimeField(null=True, verbose_name=b'date of selction', blank=True)),
                ('date_of_match', models.DateTimeField(null=True, verbose_name=b'date of match', blank=True)),
                ('place', models.CharField(max_length=20, null=True, blank=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('gender', models.CharField(max_length=10)),
                ('friends_count', models.IntegerField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='entrychoice',
            name='choice',
            field=models.ForeignKey(to='valentine.UserEntry'),
            preserve_default=True,
        ),
    ]
