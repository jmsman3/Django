from django.shortcuts import render ,redirect
from category_app.forms import CategoryForm
from . import forms
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('ShowPage')
    else:
        form =CategoryForm()
    return render(request , 'category.html', {'form' : form})