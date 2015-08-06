# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materialapp', '0005_producttype_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttype',
            old_name='profile_image',
            new_name='image',
        ),
    ]
