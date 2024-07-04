from django.shortcuts import render
from first_app.forms import ExampleForm,MyModelForm

# Create your views here.
def index(request):
    form = ExampleForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
        else:
            form = ExampleForm()
    return render(request , 'index.html' ,{'form':form})

def modell(request):
    form = MyModelForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print('abs')
            print(form.cleaned_data)
        else:
            form = MyModelForm()
    return render(request , 'modell.html' ,{'form':form})