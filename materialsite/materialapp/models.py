#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

import os

def get_image_path(instance, filename):
    return os.path.join('photos', filename)


# Model to Register a simple Category in App
class Category(models.Model):
	name = models.CharField(max_length=128, verbose_name='nome')
	description = models.TextField(verbose_name='descrição')

	class Meta:
		# ordena a exibicao do admin pelo nome
		ordering = ['name']
		verbose_name = 'categoria'
		verbose_name_plural = 'categorias'

	#convenience when describe something on admin
	def __unicode__(self):
		return self.name

# Model to Register a product type (tintas, vasos, portas, janelas, fechaduras, etc)
class ProductType(models.Model):
	name = models.CharField(max_length=200, verbose_name='nome')
	description = models.TextField(verbose_name='descrição')
	image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	categories = models.ManyToManyField(Category)
	
	
	class Meta:
		# ordena a exibicao do admin pelo nome
		ordering = ['name']
		verbose_name = 'tipo de produto'
		verbose_name_plural = 'tipos de produto'

	#convenience when describe something on admin
	def __unicode__(self):
		return self.name



# Model to Register a device (android, ios, windowsphone etc)
DEVICE_CHOICES = ( ('1', 'android'), ('2', 'ios'))
class Device(models.Model):
	device_type = models.CharField(choices=DEVICE_CHOICES, default='android', max_length=64, verbose_name='tipo')
	device_id = models.CharField(max_length=128, verbose_name='identificador')
	
	class Meta:
		# ordena por tipo
		ordering = ['device_type']
		verbose_name = 'dispositivo'
		verbose_name_plural = 'dispositivos'

	#detail
	def __unicode__(self):
		return self.device_id


