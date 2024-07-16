from typing import Any
from django.shortcuts import render , redirect
from Category.forms import CarForm ,BrabdForm , CommentForm
from Category.models import CarModel , CategoryModel ,Order
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
    return render(request , 'home.html', {'data' : data , 'category' : categories})

@login_required
def carpost(request):
    if request.method == 'POST': 
        post_form = CarForm(request.POST , request.FILES)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('home')
    else:
        post_form = CarForm()
    return render(request , 'post.html' , {'form' : post_form})

@login_required
def brandpost(request):
    if request.method == 'POST': 
        post_form = BrabdForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('carpost')
    else:
        post_form = BrabdForm()
    return render(request , 'add_brand.html' , {'form' : post_form})

   #-----------------------------------------------------DetailPost is Class based View----------------------------------------
@method_decorator(login_required, name='dispatch')
class DetailPostView(DetailView):
    model = CarModel
    pk_url_kwarg = 'id'
    template_name ='detail_post.html'

    def post(self,request,  *args, **kwargs):
        comment_form = CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request , *args , **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # Carmodel er object eikhane show koralam
        comments = post.comments.all()
        comment_form = CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


@login_required
def buy_car(request,id):
    car = CarModel.objects.get(pk = id)
    if car.quantity is not None and car.quantity > 0:
        car.quantity -= 1
        car.save()
        #order entry creat :
        order =  Order.objects.create(buyer=request.user , car=car)
        messages.success(request,'You have Successsfully Bought the car')
    else:
        messages.warning(request ,'Sorry, the car is out of stock')   
    return redirect('profile')

@login_required
def profile(request):
    orders = Order.objects.filter(buyer=request.user)
    print(orders)
    return render(request,'profile.html',{'purchases' : orders})



