from django.shortcuts import render
from .forms import ContactForm


def home_page(request):
	context = {"title":"Home Page",
				"content":"Welcome to Home Page"
				}
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
	# if request.method == 'POST':
	# 	print (request.POST)
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	return render(request,"contact/view.html",context)
