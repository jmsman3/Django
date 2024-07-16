from . models import MusicianModel , AlbumModel
from django import forms 
from django.forms import DateInput
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserChangeForm , UserCreationForm  
class MusicianForm(forms.ModelForm):
    class Meta:
        model = MusicianModel
        fields = '__all__'
    
class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel 
        fields = '__all__'
        widgets = {
            'album_release_date' : DateInput(attrs= {'type' : 'date'}),
            'rating': forms.Select(choices=AlbumModel.rate_choices)
        }

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email =forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    
    class Meta:
        model = User
        fields = ['username' ,'first_name' , 'last_name' , 'email']




