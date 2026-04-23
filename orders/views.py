from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is home page")

def order_list(request):
    return HttpResponse("This is the orders page.")