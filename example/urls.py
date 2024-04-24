from django.urls import path
from . import views
from .views import base


urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('base', views.base, name='base'),
    path('cart', views.cart, name='cart'),
    path('index', views.index, name='index'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('shop', views.shop, name='shop'),
    path('shopdetail', views.shopdetail, name='shopdetail'),
    path('testimonial', views.testimonial, name='testimonial'),
]
