# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='map_data',
            field=models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to=b'maps'),
        ),
    ]
