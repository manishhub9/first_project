from django.shortcuts import render

def cart_home(request):
    # print (request.session)
    # print(dir(request.session))
    # key = request.session.session_key
    # print('keys is ',key)
    # request.session['cart_id'] = 12
    return render(request,'carts/home.html',{})
