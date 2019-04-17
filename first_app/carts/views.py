from django.shortcuts import render, redirect
from .models import Cart
from orders.models import Order
from accounts.models import GuestEmail
from products.models import Product
from accounts.forms import LoginForm, GuestForm
from address.forms import AddressForm
from billing.models import BillingProfile

def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	return render(request,'carts/home.html',{'cart':cart_obj})

def checkout_home(request):
	cart_obj, cart_created = Cart.objects.new_or_get(request)
	order_obj = None
	if cart_created or cart_obj.products.count() == 0:
		return redirect("cart:home")
	billing_profile = None
	login_form = LoginForm()
	guest_form = GuestForm()
	address_form = AddressForm()
	blling_address_form = AddressForm()
	billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
	if billing_profile is not None:
		order_obj = Order.objects.new_or_get(billing_profile,cart_obj)
	context = {"object":order_obj,
				"billing_profile":billing_profile,
				"login_form":login_form,
				"guest_form":guest_form,
				"address_form":address_form,
				"blling_address_form":blling_address_form
				}
	return render(request,'carts/checkout_home.html',context)

def cart_update(request):
	product_id = request.POST.get('product_id')
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			print("product not found.")
			return redirect("cart:home")
		cart_obj, new_obj = Cart.objects.new_or_get(request)
		if product_obj in cart_obj.products.all():
			cart_obj.products.remove(product_obj)
		else:
			cart_obj.products.add(product_obj)
		request.session["cart_items"] = cart_obj.products.count()
	return redirect("cart:home")
