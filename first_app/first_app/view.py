from django.shortcuts import render, redirect
from .forms import ContactForm

def home_page(request):
	# print(request.session.get('first_name'))
	context = {"title":"Home Page",
				"content":"Welcome to Home Page"
				}
	if request.user.is_authenticated():
		context["premium_content"] = "Yeahhhhh"
	print('method invoke..home_page')
	return render(request,"home.html",context)

def about_page(request):
	print('method invoke..about_page')
	context = {"title":"About Page",
				"content":"Welcome to About Page"}
	return render(request,"home.html",context)

def contact_page(request):
	print('method invoke__contact_page')
	contact_form = ContactForm(request.POST or None)
	context = {"title":"Contact Page",
				"content":"Welcome to Contact Page",
				"form":contact_form
				}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	return render(request,"contact/view.html",context)
