from django.shortcuts import render
from django.http import HttpResponse
from .models import Order

def home(request):
    return HttpResponse("This is home page")

def order_list(request):
    orders = Order.objects.all() # pylint: disable=no-member
    return render(request, 'orders/orders_list.html', {"orders": orders})