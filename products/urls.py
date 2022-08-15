from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='home'),
    path('productdetails/<int:pk>',views.productdetails, name = 'productsdetails'),
    path('categories/', views.categories, name='categories'),
    path('addProducts/', views.addProducts, name = 'addProducts'),
    path('deleteProduct/', views.deleteProduct, name='deleteProduct'),
    path('cartitems/',views.cartitems, name = 'cartitems'),
    path('productdetails/cart/',views.cart, name = 'cart'),

    ]
