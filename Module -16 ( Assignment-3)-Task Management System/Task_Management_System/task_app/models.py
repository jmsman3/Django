from django.db import models
from category_app.models import CategoryModel
# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    Task_Assign_Date = models.DateField()
    Catagories = models.ManyToManyField(CategoryModel)
    is_Completed = models.BooleanField(default= False)

    def __str__(self):
        return f"{self.title}"