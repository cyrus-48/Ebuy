from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='home'),
    path('categories/', views.categories, name='categories'),
    path('addProducts/', views.addProducts, name = 'addProducts'),
    path('deleteProduct/', views.deleteProduct, name='deleteProduct'),

    ]
