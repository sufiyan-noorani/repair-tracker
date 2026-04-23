from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('orders/', views.order_list),
]