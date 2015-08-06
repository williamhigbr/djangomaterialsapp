# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import materialapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('materialapp', '0004_producttype_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=materialapp.models.get_image_path, blank=True),
        ),
    ]
