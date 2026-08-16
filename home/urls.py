from django.urls import path
from . import views

urlpatterns = [
    path('base_page/', views.base, name='base_page'),
    path('san-pham/<int:id>/', views.product_details, name='product_details'),
]