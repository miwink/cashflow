# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20170313_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file_path',
        ),
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='firebase_instance_id',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
