from django.shortcuts import render , redirect
from Car_Author.forms import RegistrationForm  , Edit_Profile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , SetPasswordForm , PasswordChangeForm
from django.contrib.auth import authenticate , login , logout , update_session_auth_hash
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm 
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
def home(request):
    return render(request , 'home.html')

def profile(request):
    return render(request , 'profile.html')

def signup_user(request): 
    if not request.user.is_authenticated:
        if request.method =='POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data['first_name']
                user_2 = form.cleaned_data['last_name']
                messages.success(request , f"{user} {user_2}, Account Created Succcessfully")
                print(form.cleaned_data)
                return redirect('login')
        else:
            form = RegistrationForm()
        return render( request , 'signup.html' ,{'form' : form})
    else:
        return redirect('home')
    
    #-----------------------------------------------------Signup is Class based View----------------------------------------
class SignupClass(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user_name = form.cleaned_data.get('username')
        messages.success(self.request ,f"Congratulations ,{user_name} - Your Account Created Successfully" )
        return super().form_valid(form)
    
    def  dispatch(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch( *args, **kwargs)

def login_user(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form = AuthenticationForm(request=request , data =request.POST) #user er kache theke data nelam
            if form.is_valid():
                name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username = name , password = user_pass) #check kori user database e ase kina
                if user is not None:
                    messages.success(request , f"Hey, {name} -your Login Succcessfull")
                    login(request , user)
                    return redirect('home')
                else:
                    messages.warning(request , 'Please enter Correct information')

        else:
            form = AuthenticationForm()
        return render(request , 'login.html' , {'form' : form})
    else:
        return redirect('profile')


            
def logout_user(request):
    logout(request)
    return redirect('login')

def edit_profile(request):
    if  request.user.is_authenticated:
        if request.method =='POST':
            form = Edit_Profile(request.POST , instance= request.user) #user er kache theke data nelam
            if form.is_valid():
                form.save()
                user = form.cleaned_data['first_name']
                user_2 = form.cleaned_data['last_name']
                messages.success(request , f"{user} {user_2}, Your Profile Updated Succcessfully")          
        else:
            form = Edit_Profile(instance = request.user)
        return render(request , 'edit_profile.html' , {'form' : form})
    else:
        return redirect('signup')
    



   #-----------------------------------------------------Edit Person Biodata is Class based View----------------------------------------

@method_decorator(login_required, name='dispatch')
class Edit_PersonCLass(generic.UpdateView):
    model = User
    form_class = Edit_Profile
    template_name = 'edit_profile.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.cleaned_data['first_name']
        user_2 = form.cleaned_data['last_name']
        messages.success(self.request, f"{user} {user_2}, Your Profile Updated Successfully")
        return response

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('signup')
        return super().dispatch(request, *args, **kwargs)






def password_change(request):
    if  request.user.is_authenticated:
        if request.method =='POST':
            form = PasswordChangeForm( request.user , data = request.POST) #user er kache theke data nelam
            if form.is_valid():
                form.save()
                messages.success(request , f" Your Password Updated Succcessfully")       
                update_session_auth_hash(request , form.user)
                return redirect('profile')   
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request , 'pass_change.html' , {'form' : form})
    else:
        return redirect('login')

