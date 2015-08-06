#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

#import models
from .models import Category
from .models import ProductType
from .models import Device

# Register your models here.
#admin.site.register(Category)

# Admin Elements
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')
	list_filter = ('name', )

class DeviceAdmin(admin.ModelAdmin):
	list_display = ('device_type', 'device_id')
	list_filter = ('device_type', )
	search_fields = ['device_id']


# admin registers
admin.site.register(Category, CategoryAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(ProductType)