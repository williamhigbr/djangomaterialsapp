# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materialapp', '0002_auto_20150804_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'nome')),
                ('description', models.TextField(verbose_name=b'descri\xc3\xa7\xc3\xa3o')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'tipo de produto',
                'verbose_name_plural': 'tipos de produto',
            },
        ),
    ]
