from django.shortcuts import render ,redirect
from task_app.forms import TaskForm 
from  task_app.models import TaskModel
from . import forms
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('ShowPage') 
    else:
        form = TaskForm()
    return render(request , 'task.html' ,{'form' : form})

def show_task(request):
    data = TaskModel.objects.all()

    return render(request , 'show_task.html' , {'data': data})
        
def edit_post(request ,id):
    post = TaskModel.objects.get(pk = id)
    post_form = TaskForm(instance=post)
    if request.method == 'POST':
        post_form = TaskForm( request.POST ,instance=post)
        if post_form.is_valid():
            post_form.save()       
            return redirect('ShowPage') 
    return render(request , 'task.html', {'form' : post_form} )

def delete_post(request ,id):
    post = TaskModel.objects.get(pk = id)
    post.delete()
    return redirect('ShowPage') 
