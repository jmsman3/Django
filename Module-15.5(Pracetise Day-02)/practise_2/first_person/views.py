from django.shortcuts import render , redirect
from first_person.forms import MuscianForm  ,AlbumForm
from first_person.models import  Musician , AlbumModel
from itertools import chain
from . import models
from . import forms


# Create your views here.
def person(request):
    form = MuscianForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('albumpage')
    else:
        form = MuscianForm()
    return render(request , 'person.html' , {'form':form})

def album(request):
    form = AlbumForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('homepage')
    else:
        form = AlbumForm()
    return render(request , 'album.html' , {'form':form})



def home(request):

    data = AlbumModel.objects.all()
    # print(data) 
    # for i in data:
    #     print(i.first_name)
    #     for j in data2.all():
    #         print(j)
    return render(request , 'home.html' , {'data':data})


def delete_musician(request, id):
    target_person = models.AlbumModel.objects.get(pk = id)
    target_person.delete()
    return redirect('homepage')


def edit_person(request, id):
    album_instance= Musician.objects.get(pk=id) 
    form = forms.MuscianForm(instance= album_instance)
    if request.method == 'POST': 
        form = forms.MuscianForm( request.POST ,instance= album_instance)
        if form.is_valid(): 
            form.save() 
            return redirect('albumpage')
    
    return render(request, 'person.html', {'form' : form})


def album_edit(request, id):
    album_instance= AlbumModel.objects.get(pk=id) 
    form = forms.AlbumForm(instance= album_instance)
    if request.method == 'POST': 
        form = forms.AlbumForm( request.POST ,instance= album_instance)
        if form.is_valid(): 
            form.save() 
            return redirect('homepage')
    
    return render(request, 'album.html', {'form' : form})

