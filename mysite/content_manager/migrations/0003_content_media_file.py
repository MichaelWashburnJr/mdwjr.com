# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_manager', '0002_auto_20150513_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='media_file',
            field=models.FileField(upload_to='', null=True, blank=True),
            preserve_default=True,
        ),
    ]
