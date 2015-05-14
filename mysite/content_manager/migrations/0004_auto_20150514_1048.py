# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import content_manager.models
import content_manager.storage


class Migration(migrations.Migration):

    dependencies = [
        ('content_manager', '0003_content_media_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='media_file',
        ),
        migrations.AddField(
            model_name='content',
            name='media',
            field=models.FileField(null=True, upload_to=content_manager.models.file_path, blank=True, storage=content_manager.storage.OverwritesStorage()),
            preserve_default=True,
        ),
    ]
