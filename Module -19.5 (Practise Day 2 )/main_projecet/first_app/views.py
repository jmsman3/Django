from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render ,redirect
from first_app.forms import MusicianForm , AlbumForm , RegistrationForm
from first_app.models import MusicianModel , AlbumModel
from django.contrib import messages
from django.contrib.auth import authenticate  ,login , logout ,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm ,SetPasswordForm ,PasswordChangeForm
from django.contrib.auth import forms 

#class view import 
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView 
from django.views import View

# Create your views here.
#______________________________________________for add person(Function + Class)__________________________________________
def person(request):
    if request.user.is_authenticated:
        form = MusicianForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                print(form.cleaned_data)
                messages.success(request , f"Congratulations , Musician Added Successfully")
                form.save()
                return redirect('album_page')
        else:
            form = MusicianForm()
        return render(request , 'person.html' , {'form' : form})
    else:
        return redirect('home_page')
    
@method_decorator(login_required, name='dispatch')
class PersonView(View):
    def get(self, request):
        form = MusicianForm()
        return render(request, 'person.html', {'form': form})

    def post(self, request):
        form = MusicianForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations, Musician Added Successfully")
            form.save()
            return redirect('album_page')
        return render(request, 'person.html', {'form': form})  
    
#______________________________________________for add Album(Function + Class)_____________________________________
def album(request):
    if request.user.is_authenticated:
        form = AlbumForm(request.POST)
        if request.method =='POST':
            if form.is_valid():
                print(form.cleaned_data)
                messages.success(request , f"Congratulations ,Album Added Successfully")
                form.save()
                return redirect('profile_page')
        else:
            form = AlbumForm()
        return render( request , 'album.html' , {'form' : form})
    else:
        return redirect('home_page')
    
@method_decorator(login_required, name='dispatch')
class AlbumView(View):
    def get(self, request):
        form = AlbumForm()
        return render(request, 'album.html', {'form': form})

    def post(self, request):
        form = AlbumForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations, Musician Added Successfully")
            form.save()
            return redirect('profile_page')
        return render(request, 'album.html', {'form': form})  

def home(request):
    data = AlbumModel.objects.all()
    return render( request , 'home.html' , {'data' : data})


#______________________________________________for SignUp(Function + Class)__________________________________________
def SignUp(request):
    if not request.user.is_authenticated:
            
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user_name = form.cleaned_data.get('username')
                messages.success(request , f"Congratulations ,{user_name} - Your Account Created Successfully")
                form.save()
                return redirect('login_page')
        else:
            form = RegistrationForm()
        return render(request , 'signup.html' , {'form' : form})
    else:
        return redirect('home_page')
    
# @method_decorator(login_required , name='dispatch')
class SignupClass(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login_page')
    
    def form_valid(self, form):
        user_name = form.cleaned_data.get('username')
        messages.success(self.request ,f"Congratulations ,{user_name} - Your Account Created Successfully" )
        return super().form_valid(form)
    
    def  dispatch(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home_page')
        return super().dispatch( *args, **kwargs)
    
#______________________________________________for Log in (Function + Class)_________________________________________

def login_system(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request , data = request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = user_name , password = userpass)
                if user is not None:
                    messages.success(request , f"Hey,{user_name} - Your Login Successfully")
                    login(request , user)
                    return redirect('profile_page')
        else:
            form = AuthenticationForm()
        return render(request , 'login.html' , {'form' : form})
    else:
        return redirect('home_page')


class LoginClass(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('profile_page')
    
    def form_valid(self, form):
        user_name = form.cleaned_data['username']
        messages.success(self.request , f"Hey,{user_name} - Your Login Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        user_name = form.cleaned_data['username']
        messages.success(self.request , f"Hey,{user_name} - Login Information incorrect")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    

def logout_system(request):
    logout(request)
    return redirect('home_page')


def profile(request):
    data = AlbumModel.objects.all()
    return render( request , 'profile.html' , {'data' : data})

#______________________________________________for Edit Person Data(Function + Class)__________________________________________
def edit_person(request ,id):
    if  request.user.is_authenticated:
        album_instance = MusicianModel.objects.get(pk = id)
        form = MusicianForm(instance = album_instance)
        if request.method == 'POST':
            form = MusicianForm(request.POST , instance = album_instance)
            if form.is_valid():
                messages.success(request , f"Congratulations- Musician Edited Successfully")
                form.save()
                return redirect('profile_page')
        return render(request , 'person_edit.html' , {'form' : form})
    else:
        return redirect('home_page')

class Edit_PersonCLass(generic.UpdateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = 'person_edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile_page')

 #______________________________________________for album data(Function + Class)__________________________________________  
def album_edit(request ,id):
    if  request.user.is_authenticated:
        album_instance = AlbumModel.objects.get(pk = id)
        form = AlbumForm(instance = album_instance)
        if request.method == 'POST':
            form = AlbumForm(request.POST , instance = album_instance)
            if form.is_valid():
                messages.success(request , f"Congratulations - Album Edited Successfully")
                form.save()
                return redirect('profile_page')
        return render(request , 'album.html' , {'form' : form})
    else:
        return redirect('home_page')


class Edit_albumClass(generic.UpdateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile_page')

def delete_musician(request , id):
    target_person = AlbumModel.objects.get(pk = id )
    target_person.delete()
    return redirect('profile_page')

class Delete_MusicianClass(generic.DeleteView):
    model = MusicianModel
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile_page')

