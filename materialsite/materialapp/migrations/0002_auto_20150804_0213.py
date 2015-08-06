# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materialapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_type', models.CharField(default=b'android', max_length=64, verbose_name=b'tipo', choices=[(b'1', b'android'), (b'2', b'ios')])),
                ('device_id', models.CharField(max_length=128, verbose_name=b'identificador')),
            ],
            options={
                'ordering': ['device_type'],
                'verbose_name': 'dispositivo',
                'verbose_name_plural': 'dispositivos',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name=b'descri\xc3\xa7\xc3\xa3o'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=128, verbose_name=b'nome'),
        ),
    ]
