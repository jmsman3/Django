from django import forms   
from django.forms.widgets import SelectDateWidget
import datetime 
from first_app.models import ModelForom 
# from .models import MyModel

class ExampleForm(forms.Form):
    name = forms.CharField(label="Enter Your name here")
    email = forms.EmailField(label='Enter Your email here')
    age = forms.IntegerField(label="Enter your age here")
    roll_numer = forms.IntegerField(help_text='Enter 6 digit Roll number')
    passWord = forms.CharField(widget=forms.PasswordInput())
    name = forms.CharField(label="Enter Your name here")
    email = forms.EmailField(label='Enter Your email here')
    age = forms.IntegerField(label="Enter your age here")
    comment = forms.CharField(widget= forms.Textarea(attrs={'rows':3}))
    date = forms.DateField()
    Birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    Birth_year_choices = ['1980', '1981','1982']
    birth_year = forms.DateField(widget=SelectDateWidget(years = Birth_year_choices))

    value = forms.DecimalField()
    email_address = forms.EmailField(required=False, initial="Provide email")
    name = forms.CharField( initial='Your name')
    agreee = forms.BooleanField(initial=True)
    to_day = forms.DateField(initial=datetime.date.today)

    # ChoiceField() Use kora

    favourite_color_choices = [('b','blue'), ('g','green'), ('r', 'red')]
    favourite_Color = forms.ChoiceField(choices=favourite_color_choices ,label='Your Priyo Color')
    fav_color_with_Radiio_button = forms.ChoiceField(widget= forms.RadioSelect , choices=favourite_color_choices)
    multiple_ChoiceField = forms.MultipleChoiceField(choices=favourite_color_choices)
    multiple_ChoiceField_with_CHECKBOX = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple , choices= favourite_color_choices)

  
class MyModelForm(forms.ModelForm):
    class Meta:
         model = ModelForom
         fields = '__all__'