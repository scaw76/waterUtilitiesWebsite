# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicNotices', '0002_noticefile_notice_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticefile',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]