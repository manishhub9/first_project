from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product
from carts.models import Cart
from django.http import Http404

class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = 'products/list.html'
	def get_context_data(self,*args,**kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		cart_obj,new_obj = Cart.objects.new_or_get(self.request)
		context['cart'] = cart_obj
		return context

class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = 'products/detail.html'
	def get_context_data(self,*args,**kwargs):
		context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
		cart_obj,new_obj = Cart.objects.new_or_get(self.request)
		context['cart'] = cart_obj
		return context
