# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-07 18:05
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


def detect_available_assets(apps, schema_editor):
    Task = apps.get_model('app', 'Task')

    for t in Task.objects.all():
        print("Updating {}".format(t))
        t.update_available_assets_field(True)


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170707_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='available_assets',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=80), blank=True, default=[], help_text='List of available assets to download', size=None),
        ),
        migrations.RunPython(detect_available_assets),
    ]
