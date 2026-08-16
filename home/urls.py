from django.urls import path
from . import views

urlpatterns = [
    path('base_page/', views.base, name='base_page'),
    path('/', views.home,name='home'),
    
]
