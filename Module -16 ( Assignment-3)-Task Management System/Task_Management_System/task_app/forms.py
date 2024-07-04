from django import forms
from django.forms import DateInput ,CheckboxSelectMultiple
from task_app.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        widgets = {
            'Task_Assign_Date' : DateInput(attrs={'type':'date'}),
            'Catagories' : CheckboxSelectMultiple, 
        }
        help_texts = {
            'title':'Enter title within 100 characters'  ,
            'Catagories':'choose single or multiple option as you need'  ,
            'is_Completed' :'if your task is Fulfil-Mark this checkbox'
        }
        labels ={
            'title':'Enter Title',
            'description':'Enter Description',
            'Task_Assign_Date':'Enter your task assign date',
            'Catagories':'Enter your categories',
        }