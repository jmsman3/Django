from django import forms
from django.forms import DateInput
from category_app.models import CategoryModel
class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = '__all__'

        help_texts = {
            'Category_Name': 'Enter category name within 100 character',
        }
        labels ={
            'Category_Name': 'Enter Category Name'
        }
            