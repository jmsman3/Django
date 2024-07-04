from django import forms
from first_person.models import Musician ,AlbumModel 
from django.forms import DateInput
class MuscianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'



class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = '__all__'
        widgets = {
             'Album_Realease_Date' : DateInput(attrs={'type':'date'}) ,
             }

