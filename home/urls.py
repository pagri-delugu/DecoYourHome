from django.urls import path
from . import views

urlpatterns = [
    path('base_page/', views.base, name='base_page'),
    path('', views.home, name='home'),
    path('tim-kiem/', views.search, name='search'),
    path('san-pham/', views.product_list, name='product_list'),
    path('san-pham/<int:id>/', views.product_details, name='product_details'),
    path('lien-he/', views.contact, name='contact'),
    path('tin-tuc/', views.news, name='news'),
    path('tin-tuc/<int:id>/', views.news_article, name='news_article'),
]