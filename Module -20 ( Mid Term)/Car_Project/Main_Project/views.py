
from django.shortcuts import render , redirect
from Category.forms import CarForm ,BrabdForm , CommentForm
from Category.models import CarModel , CategoryModel
from django.views.generic import DetailView 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
def home(request , category_slug = None):
    data = CarModel.objects.all()
    if category_slug is not None:
        category = CategoryModel.objects.get(slug = category_slug)
        data = CarModel.objects.filter( brand = category )
    categories = CategoryModel.objects.all()
    print(data)
    return render(request , 'home.html', {'data' : data , 'category' : categories})