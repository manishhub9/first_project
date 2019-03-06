from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product
from django.http import Http404

class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = 'products/list.html'

class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = 'products/detail.html'
