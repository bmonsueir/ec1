from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q #what is?
from .forms import UserForm #, ProjectForm, GroupForm
import simplejson as json
from django.http import HttpResponse
from django.template.context import RequestContext


def home(request):
    return render(request, 'product/home.html')

def about(request):
    return render(request, 'product/home.html')

def contact(request):
    return render(request, 'product/home.html')

def products(request):
    return render(request, 'product/home.html')

def product(request):
    return render(request, 'product/home.html')
