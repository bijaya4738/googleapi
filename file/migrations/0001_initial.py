# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('map_name', models.CharField(max_length=200)),
                ('map_data', models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to=b'/maps')),
            ],
        ),
    ]
