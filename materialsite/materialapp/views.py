#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import Http404
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CategoryList(APIView):
	def post(self, request, format=None):
		categories = Category.objects.all()
		serializer = CategorySerializer(categories, many=True)
		return Response(serializer.data)


class ProductTypeList(APIView):
	def post(self, request, format=None):
		product_types = ProductType.objects.all()
		serializer = ProductTypeSerializer(product_types, many=True)
		return Response(serializer.data)