from django.urls import path
from . import views
from .views import index


urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('index', views.index, name='index'),
    
]
