from django.urls import path
from . import views
from .views import checkout


urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove_cartitem/<int:product_id>/', views.remove_cartitem, name='remove_cartitem'),
    path('checkout', views.checkout, name='checkout'),
]
