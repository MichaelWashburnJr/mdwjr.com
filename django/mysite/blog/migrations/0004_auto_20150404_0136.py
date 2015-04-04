# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150403_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=20, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.CharField(max_length=20, db_index=True),
            preserve_default=True,
        ),
    ]
