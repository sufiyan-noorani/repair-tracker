from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order

def home(request):
    return HttpResponse("This is home page")

def order_list(request):
    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        device_name = request.POST.get("device_name")
        quantity = request.POST.get("quantity")

        if customer_name and device_name and quantity:
            Order.objects.create(   # pylint: disable=no-member
                customer_name = customer_name,
                device_name = device_name,
                quantity = quantity
                )
            return redirect('order_list')

    orders = Order.objects.all() # pylint: disable=no-member
    return render(request, 'orders/orders_list.html', {"orders": orders})