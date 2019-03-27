from django.shortcuts import render
from django.views.generic import ListView, DetailView
from products.models import Product


class SearchProductView(ListView):
	queryset = Product.objects.all()
	template_name = 'products/list.html'
	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.filter(title__icontains='Bed')
