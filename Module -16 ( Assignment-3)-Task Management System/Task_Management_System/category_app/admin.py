from django.contrib import admin
from category_app.models import CategoryModel
from task_app.models import TaskModel
# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(TaskModel)
