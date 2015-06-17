# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import content_manager.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, blank=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('body', models.TextField(null=True, blank=True)),
                ('media', models.FileField(storage=content_manager.storage.OverwritesStorage(), null=True, upload_to='', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='content',
            name='page',
            field=models.ForeignKey(related_name='content_set', to='content_manager.Page'),
            preserve_default=True,
        ),
    ]
