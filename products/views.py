from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q #what is?
import simplejson as json
from django.http import HttpResponse
from django.template.context import RequestContext
from .models import Product

def home(request):
    return render(request, 'products/home.html')

def about(request):
    return render(request, 'products/about.html')

def contact(request):
    return render(request, 'products/contact.html')

def products(request):
    return render(request, 'products/products.html')

def product(request):
    return render(request, 'products/product.html')
