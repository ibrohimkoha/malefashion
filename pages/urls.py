# import
from django.urls import path
from . import views
# app name
app_name = 'pages'

urlpatterns = [
    # urls
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('blog/', views.blog, name='blog'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('shop_details/', views.shop_details, name='shop_details'),
    path('shop/', views.shop, name='shop'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart')
]