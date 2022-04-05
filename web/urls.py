from django.urls import path

from . import views

app_name='web'

urlpatterns = [
    path('', views.index,name='index'),
    path('menu/', views.menu,name='menu'),
    path('gallery/', views.gallery,name='gallery'),
    path('contact/', views.contact,name='contact'),

    path('cart/', views.cart,name='cart'),

    #ajax calling for cart
    path('add-cart/', views.add_cart,name='add_cart'),

    path('update-cart/',views.update_cart, name='increment'),
    path('delete-cart/',views.cart_delete, name='decrement'),
]