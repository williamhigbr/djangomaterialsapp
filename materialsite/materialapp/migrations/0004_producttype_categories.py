# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materialapp', '0003_producttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='categories',
            field=models.ManyToManyField(to='materialapp.Category'),
        ),
    ]
