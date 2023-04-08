from django.urls import path
from . import views

urlpatterns = [
    #path('order_detail/', views.order_detail, name='order_detail'),
    path('payments/', views.payments, name='payments'),
    path('payments/order_complete', views.order_complete, name='order_complete'),
]
