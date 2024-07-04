from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label="Full name" , 
    initial='Rahim Uddin', disabled=False,help_text="Total length must be within 70 character",
    widget=forms.Textarea(attrs= {'id': 'text_area', 'class':'class1 class2', 'placeholder':'Enter Your Name'}), error_messages={'required': 'Please enter your name.'},
    )
    # file = forms.FileField()
    email = forms.EmailField(label="User Email") 
    # age = forms.IntegerField()
    age = forms.CharField(widget=forms.NumberInput)
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday =forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment =forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))

    CHOICES = [('S', 'Small') , ('M' , 'Medium') , ('L' , 'Large')]
    size = forms.ChoiceField(choices= CHOICES , widget=forms.RadioSelect)

    MEAL = [('P', 'Pepperoni') , ('M', 'Mashroom') , ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices= MEAL , widget=forms.CheckboxSelectMultiple)

    
# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 Character")
    #     return valname
    
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com")
    #     return valemail

    #eksathe korte chiale aivhabe korte hobe

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']

    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter a name with atleast 10 character")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com") 

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 chars")

class StudentData(forms.Form):
    name = forms.CharField( validators=[validators.MinLengthValidator(10, message="Enter a name at least 10 Characters")])

    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid email")]) 

    age = forms.IntegerField(validators=[validators.MaxValueValidator(34 ,message="Maximum age value is 34")
    ,validators.MinValueValidator(24, message="Minume age value Start fom 24")])
   
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'png'], message="Only .Pdf and .png is Allow Here")])

    text = forms.CharField(widget=forms.TextInput, validators=[len_check])


class PasswordValidationForm(forms.Form):
    name = forms.CharField(widget= forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    Confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_name = self.cleaned_data['name']
        val_password = self.cleaned_data['password']
        val_ConfirmPassword = self.cleaned_data['Confirm_password']
        if val_password != val_ConfirmPassword:
            raise forms.ValidationError("Password does not match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 characters")
        



    