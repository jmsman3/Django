from Category.models import CarModel , CategoryModel ,Comment
from django import forms
class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        # fields = '__all__'
        exclude = ['author']

class BrabdForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        # fields = '__all__'
        exclude = ['slug']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name' , 'email' , 'body']
        

