from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")

def base(request):
    return render(request, 'base.html')
 
def cart(request):
    return render(request, 'bootstrap/cart.html')

def index(request):
    return render(request, 'bootstrap/index.html')

def checkout(request):
    return render(request, 'bootstrap/checkout.html')

def shopdetail(request):
    return render(request, 'bootstrap/shop-detail.html')

def shop(request):
    return render(request, 'bootstrap/shop.html')

def testimonial(request):
    return render(request, 'bootstrap/testimonial.html')

def contact(request):
    return render(request, 'bootstrap/contact.html')
